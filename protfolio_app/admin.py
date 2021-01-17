from django.contrib import admin
from .models import Footer_Header,About_me,Contact,Skills,Education,Category,project,Service,Protfolio_Category,Protfolio,FAQ,Experience_project

# Register your models here.

admin.site.register(Category)
admin.site.register(Protfolio_Category)
admin.site.register(project)
admin.site.register(Protfolio)

admin.site.register(Skills)
admin.site.register(Service)
admin.site.register(Education)
admin.site.register(Contact)

admin.site.register(Footer_Header)
admin.site.register(About_me)
admin.site.register(FAQ)
admin.site.register(Experience_project)