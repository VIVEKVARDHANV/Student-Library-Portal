from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    # path('upload/', views.upload_pdf, name='upload_pdf'),
    path('upload_bme/', views.upload_pdf_bme, name='upload_pdf_bme'),
    path('upload_maths/', views.upload_pdf_maths, name='upload_pdf_maths'),
    path('upload_be/', views.upload_pdf_be, name='upload_pdf_be'),
    path('upload_chem/', views.upload_pdf_chem, name='upload_pdf_chem'),
    path('upload_mos/', views.upload_pdf_mos, name='upload_pdf_mos'),
    path('display/', views.display_pdf, name='display_pdf'),
    path('display_maths/', views.display_maths, name='display_math'),
    path('display_bme/', views.display_bme, name='display_bme'),
    path('display_chem/', views.display_chem, name='display_chem'),
    path('display_be/', views.display_be, name='display_be'),
    path('display_mos/', views.display_be, name='display_mos'),
    path('pdf/display_be/<str:success_message>/', views.display_be, name='display_be'),
    path('pdf/display_bme/<str:success_message>/', views.display_be, name='display_be'),
    path('pdf/display_mos/<str:success_message>/', views.display_be, name='display_be'),
    path('pdf/display_chem/<str:success_message>/', views.display_be, name='display_be'),
    path('pdf/display_maths/<str:success_message>/', views.display_be, name='display_be'),
    path('display/<str:success_message>/', views.display_pdf, name='display_pdf_with_message'),  # Add this line
    path('reward_selection/', views.reward_selection, name='reward_selection'),
    path('first/', views.first_year, name='first'),
    path('second/', views.second_year, name='second'),
    path('third/', views.third_year, name='third'),
    path('fourth/', views.fourth_year, name='fourth'),
    

]
