from django.contrib import admin
from .models import Footer_Header, About_me, Contact, Skills, Education, Project_Category, project, Service, \
    Protfolio_Category, \
    Protfolio, FAQ, Experience_project


# Register your models here.


class project_admin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'create_at', 'update_at']
    search_fields = ["title", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = project


admin.site.register(project, project_admin)


class Project_Category_admin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'update_at']
    search_fields = ["name", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = Project_Category


admin.site.register(Project_Category, Project_Category_admin)


class Portfolio_Category_admin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'update_at']
    search_fields = ["name", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = Protfolio_Category


admin.site.register(Protfolio_Category, Portfolio_Category_admin)


class Portfolio_admin(admin.ModelAdmin):
    list_display = ['title', 'pro_category', 'image_tag', 'create_at', 'update_at']
    search_fields = ["title", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = Protfolio


admin.site.register(Protfolio, Portfolio_admin)


class Service_admin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'create_at', 'update_at']
    search_fields = ["title", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = Service


admin.site.register(Service, Service_admin)


class Skills_admin(admin.ModelAdmin):
    list_display = ['Skill_name', 'Skill_Per', 'create_at', 'update_at']
    search_fields = ["Skill_name", 'create_at']
    list_filter = ['create_at', 'Skill_name']

    class Meta:
        Model = Skills


admin.site.register(Skills, Skills_admin)


class Experience_project_admin(admin.ModelAdmin):
    list_display = ['work_category', 'work_year', 'create_at', 'update_at']
    search_fields = ["work_category", 'place_name', 'work_year']
    list_filter = ['create_at', 'work_year']

    class Meta:
        Model = Experience_project


admin.site.register(Experience_project, Experience_project_admin)


class Education_admin(admin.ModelAdmin):
    list_display = ['lavel', 'year', 'create_at', 'update_at']
    search_fields = ["lavel", 'year']
    list_filter = ['create_at', 'lavel']

    class Meta:
        Model = Education


admin.site.register(Education, Education_admin)


class Contact_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at', 'update_at']
    search_fields = ["name", 'email']
    list_filter = ['create_at', 'name', 'email']

    class Meta:
        Model = Contact


admin.site.register(Contact, Contact_admin)


class Footer_Header_admin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'email', 'create_at', 'update_at']

    # search_fields = ["sort_title"]
    # list_filter = ['Create']

    class Meta:
        Model = Footer_Header


admin.site.register(Footer_Header, Footer_Header_admin)


class About_me_admin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'email', 'update_at']

    class Meta:
        Model = About_me


admin.site.register(About_me, About_me_admin)


class FAQ_admin(admin.ModelAdmin):
    list_display = ["__str__", 'create_at', 'update_at']

    class Meta:
        Model = About_me


admin.site.register(FAQ, FAQ_admin)
