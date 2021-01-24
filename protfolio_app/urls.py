from django.urls import path
from . import views

# admin panel customization


urlpatterns = [
    path('',views.HomePage,name="home"),

    path('projects/',views.projects_page,name="projects"),
    path('project_details/<int:id>/',views.Project_details_views,name="single"),
    path('project_search/',views.project_search,name="search"),
    path('all_category_project_show/<int:id>/',views.All_category_project_show,name="all_category_project_show"),

    path('portfolio/',views.Portfolio_page,name="portfolio"),
    path('portfolio_details/<int:id>/',views.portfolio_details_View,name="single_page_2"),
    path('portfolio_search/',views.Portfolio_search,name="search2"),

    path('about_page/',views.about_page,name="about"),
    path('download_pdf/',views.download_pdf,name='download_pdf'),

    path('Resume_page/',views.Resume_page,name="resume-section"),
    path('Services/',views.Services_page,name="Services"),
    path('contact/',views.contact_page,name="contact"),





]
