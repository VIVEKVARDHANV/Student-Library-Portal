




from django.shortcuts import render, redirect
from .forms import PDFFileFormbe,PDFFileFormmaths,PDFFileFormmos,PDFFileFormbme,PDFFileFormchem
from .models import PDFFilebe,PDFFilebme,PDFFilechem,PDFFilemaths,PDFFilemos, UserPoints
# def upload_pdf(request):
#     if request.user.is_authenticated:
#         print("User is authenticated")
#         if request.method == 'POST':
#             form = PDFFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 current_user = request.user

#                 # Check if the UserPoints entry exists for the user, create if not
#                 user_points, created = UserPoints.objects.get_or_create(user=current_user)

#                 # Award 20 points to the user
#                 user_points.points += 20
#                 user_points.save()
#                 # Redirect to display_pdf page with success message
#                 return redirect('display_pdf_with_message', success_message="File uploaded successfully")
#         else:
#             form = PDFFileForm()
#         return render(request, 'upload_pdf.html', {'form': form})
#     else:
#         print("User is not authenticated")
#         # Handle case when user is not authenticated
#         # For instance, redirect to a login page or display an error message
#         return redirect('authentication:signin')  # Replace 'login_page' with your actual login page name
    
def upload_pdf_bme(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        if request.method == 'POST':
            form = PDFFileFormbme(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                current_user = request.user

                # Check if the UserPoints entry exists for the user, create if not
                user_points, created = UserPoints.objects.get_or_create(user=current_user)

                # Award 20 points to the user
                user_points.points += 20
                user_points.save()
                # Redirect to display_pdf page with success message
                return redirect('display_pdf_with_message', success_message="File uploaded successfully")
        else:
            form = PDFFileFormbme()
        return render(request, 'upload_pdf_bme.html', {'form': form})
    else:
        print("User is not authenticated")
        # Handle case when user is not authenticated
        # For instance, redirect to a login page or display an error message
        return redirect('authentication:signin')  # Replace 'login_page' with your actual login page name


def upload_pdf_chem(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        if request.method == 'POST':
            form = PDFFileFormchem(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                current_user = request.user

                # Check if the UserPoints entry exists for the user, create if not
                user_points, created = UserPoints.objects.get_or_create(user=current_user)

                # Award 20 points to the user
                user_points.points += 20
                user_points.save()
                # Redirect to display_pdf page with success message
                return redirect('display_pdf_with_message', success_message="File uploaded successfully")
        else:
            form = PDFFileFormchem()
        return render(request, 'upload_pdf_chem.html', {'form': form})
    else:
        print("User is not authenticated")
        # Handle case when user is not authenticated
        # For instance, redirect to a login page or display an error message
        return redirect('authentication:signin')  # Replace 'login_page' with your actual login page name



def upload_pdf_maths(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        if request.method == 'POST':
            form = PDFFileFormmaths(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                current_user = request.user

                # Check if the UserPoints entry exists for the user, create if not
                user_points, created = UserPoints.objects.get_or_create(user=current_user)

                # Award 20 points to the user
                user_points.points += 20
                user_points.save()
                # Redirect to display_pdf page with success message
                return redirect('display_pdf_with_message', success_message="File uploaded successfully")
        else:
            form = PDFFileFormmaths()
        return render(request, 'upload_pdf_maths.html', {'form': form})
    else:
        print("User is not authenticated")
        # Handle case when user is not authenticated
        # For instance, redirect to a login page or display an error message
        return redirect('authentication:signin')  # Replace 'login_page' with your actual login page name


def upload_pdf_mos(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        if request.method == 'POST':
            form = PDFFileFormmos(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                current_user = request.user

                # Check if the UserPoints entry exists for the user, create if not
                user_points, created = UserPoints.objects.get_or_create(user=current_user)

                # Award 20 points to the user
                user_points.points += 20
                user_points.save()
                # Redirect to display_pdf page with success message
                return redirect('display_pdf_with_message', success_message="File uploaded successfully")
        else:
            form = PDFFileFormmos()
        return render(request, 'upload_pdf_mos.html', {'form': form})
    else:
        print("User is not authenticated")
        # Handle case when user is not authenticated
        # For instance, redirect to a login page or display an error message
        return redirect('authentication:signin')  # Replace 'login_page' with your actual login page name
    
def upload_pdf_be(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        if request.method == 'POST':
            form = PDFFileFormbe(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                current_user = request.user

                # Check if the UserPoints entry exists for the user, create if not
                user_points, created = UserPoints.objects.get_or_create(user=current_user)

                # Award 20 points to the user
                user_points.points += 20
                user_points.save()
                # Redirect to display_pdf page with success message
                return redirect('display_pdf_with_message', success_message="File uploaded successfully")
        else:
            form = PDFFileFormbe()
        return render(request, 'upload_pdf_be.html', {'form': form})
    else:
        print("User is not authenticated")
        # Handle case when user is not authenticated
        # For instance, redirect to a login page or display an error message
        return redirect('authentication:signin')  # Replace 'login_page' with your actual login page name


from .models import UserPoints
from .utils import Llama  
import os 
def display_pdf(request, success_message=None):
    pdf_files = PDFFilebe.objects.all()
    os.environ['REPLICATE_API_TOKEN'] = 'r8_3sSxJb1maTZoUM3Q5YpTawbSZFInxWY2MWvBa'
    llama = Llama()
    llama_response = None
    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        llama_response = llama.generate(prompt)

    # Fetch the current user's UserPoints record
    current_user = request.user
    user_points = UserPoints.objects.get(user=current_user)  # Get the UserPoints instance for the current user

    return render(request, 'display_pdf.html', {'pdf_files': pdf_files, 'success_message': success_message,'llama_response': llama_response, 'user_points': user_points})



def display_maths(request, success_message=None):
    pdf_files = PDFFilemaths.objects.all()
    os.environ['REPLICATE_API_TOKEN'] = 'r8_3sSxJb1maTZoUM3Q5YpTawbSZFInxWY2MWvBa'
    llama = Llama()
    llama_response = None
    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        llama_response = llama.generate(prompt)

    # Fetch the current user's UserPoints record
    current_user = request.user
    user_points = UserPoints.objects.get(user=current_user)  # Get the UserPoints instance for the current user

    return render(request, 'display_maths.html', {'pdf_files': pdf_files, 'success_message': success_message,'llama_response': llama_response, 'user_points': user_points})



def display_be(request, success_message=None):
    pdf_files = PDFFilebe.objects.all()
    os.environ['REPLICATE_API_TOKEN'] = 'r8_3sSxJb1maTZoUM3Q5YpTawbSZFInxWY2MWvBa'
    llama = Llama()
    llama_response = None
    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        llama_response = llama.generate(prompt)

    # Fetch the current user's UserPoints record
    current_user = request.user
    user_points = UserPoints.objects.get(user=current_user)  # Get the UserPoints instance for the current user

    return render(request, 'display_be.html', {'pdf_files': pdf_files, 'success_message': success_message,'llama_response': llama_response, 'user_points': user_points})


def display_bme(request, success_message=None):
    pdf_files = PDFFilebme.objects.all()
    os.environ['REPLICATE_API_TOKEN'] = 'r8_3sSxJb1maTZoUM3Q5YpTawbSZFInxWY2MWvBa'
    llama = Llama()
    llama_response = None
    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        llama_response = llama.generate(prompt)

    # Fetch the current user's UserPoints record
    current_user = request.user
    user_points = UserPoints.objects.get(user=current_user)  # Get the UserPoints instance for the current user

    return render(request, 'display_bme.html', {'pdf_files': pdf_files, 'success_message': success_message,'llama_response': llama_response, 'user_points': user_points})

def display_chem(request, success_message=None):
    pdf_files = PDFFilechem.objects.all()
    os.environ['REPLICATE_API_TOKEN'] = 'r8_3sSxJb1maTZoUM3Q5YpTawbSZFInxWY2MWvBa'
    llama = Llama()
    llama_response = None
    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        llama_response = llama.generate(prompt)

    # Fetch the current user's UserPoints record
    current_user = request.user
    user_points = UserPoints.objects.get(user=current_user)  # Get the UserPoints instance for the current user

    return render(request, 'display_chem.html', {'pdf_files': pdf_files, 'success_message': success_message,'llama_response': llama_response, 'user_points': user_points})



def display_mos(request, success_message=None):
    pdf_files = PDFFilemos.objects.all()
    os.environ['REPLICATE_API_TOKEN'] = 'r8_3sSxJb1maTZoUM3Q5YpTawbSZFInxWY2MWvBa'
    llama = Llama()
    llama_response = None
    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        llama_response = llama.generate(prompt)

    # Fetch the current user's UserPoints record
    current_user = request.user
    user_points = UserPoints.objects.get(user=current_user)  # Get the UserPoints instance for the current user

    return render(request, 'display_mos.html', {'pdf_files': pdf_files, 'success_message': success_message,'llama_response': llama_response, 'user_points': user_points})




from .utils import Llama


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reward, UserPoints

import secrets

@login_required
def reward_selection(request):
    rewards = Reward.objects.all()
    user_points = UserPoints.objects.get(user=request.user)  # Fetch the current user's points

    if request.method == 'POST':
        reward_id = request.POST.get('reward_id')
        selected_reward = get_object_or_404(Reward, pk=reward_id)
        
        if user_points.points >= selected_reward.points_required:
            user_points.points -= selected_reward.points_required
            user_points.save()
            
            # Generate a random voucher code
            voucher_code = secrets.token_hex(8)  # Generates an 8-byte random code
            
            # You can use this voucher code in your display or template
            context = {
                'rewards': rewards,
                'user_points': user_points,
                'voucher_code': voucher_code  # Pass the voucher code to the template
            }
            
            return render(request, 'voucher_code.html', context)
        else:
            return render(request, 'insufficient_points.html')

    return render(request, 'reward_selection.html', {'rewards': rewards, 'user_points': user_points})


def first_year(request):
    return render(request, 'first_year.html')
def second_year(request):
    return render(request, 'second_year.html')
def third_year(request):
    return render(request, 'third_year.html')
def fourth_year(request):
    return render(request, 'fourth_year.html')
    

