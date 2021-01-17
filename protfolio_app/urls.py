from django.urls import path
from . import views

# admin panel customization


urlpatterns = [
    path('',views.HomePage,name="home"),
    path('single_post/<int:id>/',views.Single_view,name="single"),
    path('about_page/',views.about_page,name="about"),
    path('Resume_page/',views.Resume_page,name="resume-section"),
    path('Services/',views.Services_page,name="Services"),
    path('projects/',views.projects_page,name="projects"),
    path('Protfolio/',views.Protfolio_page,name="Protfolio"),
    path('contact/',views.contact_page,name="contact"),
    path('search/',views.search,name="search"),
    path('search2/',views.Protfolio_search,name="search2"),
    path('single_page_2/<int:id>/',views.single_page_2View,name="single_page_2"),
    path('download_pdf/',views.download_pdf,name='download_pdf'),

]
