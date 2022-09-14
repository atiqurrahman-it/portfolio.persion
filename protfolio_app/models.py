# 3rd party app
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField


class Footer_Header(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    my_picture = models.ImageField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()
    details = models.TextField()
    address = models.TextField(max_length=600)
    fb_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.my_picture.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class About_me(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='about_img', blank=True, null=True)
    cover_pic = models.ImageField(upload_to='cover_pic',blank=True,null=True)
    contact_sidebar_image = models.ImageField(upload_to='contact_sidebar')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()
    details = models.TextField()
    address = models.TextField(max_length=600)
    Date_of_birth = models.DateField()
    Zip_code = models.IntegerField()
    cv = models.FileField(upload_to='about_img', blank=True, null=True)
    total_project = models.IntegerField(blank=True)
    Happy_Customers = models.IntegerField(blank=True, default=20)
    total_Awards = models.IntegerField(blank=True, default=100)
    project_pending = models.IntegerField(blank=True, default=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    lavel = models.CharField(max_length=150)
    campus_name = models.CharField(max_length=220)
    year = models.CharField(max_length=10)
    details = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lavel


class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    Skill_name = models.CharField(blank=True, max_length=25)
    Skill_Per = models.IntegerField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Skill_name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    Meassage = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=300)
    category = models.ForeignKey(Project_Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_img',blank=True)
    details = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_url(self):
        return self.image.url

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Protfolio_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Protfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=300)
    pro_category = models.ForeignKey(Protfolio_Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_img',blank=True)
    details = RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=300)
    details = models.TextField(blank=True)
    image = models.ImageField(upload_to='service_img',blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title


class Experience_project(models.Model):
    id = models.AutoField(primary_key=True)
    work_category = models.CharField(max_length=150)
    place_name = models.CharField(max_length=250)
    work_year = models.CharField(max_length=10)
    details = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work_category


# faq
class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
