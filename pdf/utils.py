# # utils.py

# import replicate

# class Llama:

#   def __init__(self):
#     self.pre_prompt = "You are a helpful assistant named Claude. You respond helpfully, harmlessly, and honestly."

#   def generate(self, prompt):
    
#     output = replicate.run(
#       'anthropic/claude-alpha',
#       input={
#         'prompt': f"{self.pre_prompt}\n\nHuman: {prompt}\nClaude:"
#       }
#     )
    
#     response = ""
#     for item in output:
#       response += item
    
#     return response
  # utils/llama.py

from django.conf import settings
import replicate
import os

class Llama:
    def __init__(self):
        # Get API token from Django settings
        replicate_token = settings.REPLICATE_API_TOKEN

        # Create Replicate client and set the token in headers
        self.client = replicate.Client()
        self.client._client.headers.update({'Authorization': f'Token {replicate_token}'})
       
    def generate(self, prompt):
        output = self.client.run(
            'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
            input={
                "prompt": prompt,
                "temperature": 0.1,
                "top_p": 0.9,
                "max_length": 128,
                "repetition_penalty": 1
            }
        )

        response = ""
        for item in output:
            response += item

        return response
