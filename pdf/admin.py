# Register your models here.
from django.contrib import admin
from .models import UserPoints,Reward  # Replace with the correct import path for your UserPoints model

admin.site.register(UserPoints)
admin.site.register(Reward)
