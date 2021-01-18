from django.db import models


# Create your models here.


class Footer_Header(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField()
    details = models.TextField()
    address = models.TextField(max_length=600)
    fb_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class About_me(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    phone = models.IntegerField()
    email = models.EmailField()
    details = models.TextField()
    address = models.TextField(max_length=600)
    Date_of_birth = models.DateField()
    Zip_code = models.IntegerField()
    cv = models.FileField(blank=True, null=True)
    total_project = models.IntegerField(blank=True)
    Happy_Customers = models.IntegerField(blank=True, default=20)
    total_Awards = models.IntegerField(blank=True, default=100)
    project_pending = models.IntegerField(blank=True, default=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    lavel = models.CharField(max_length=150)
    campus_name = models.CharField(max_length=220)
    year = models.CharField(max_length=10)
    details = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lavel


class Skills(models.Model):
    Skill_name = models.CharField(blank=True, max_length=25)
    Skill_Per = models.IntegerField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Skill_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    Meassage = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class project(models.Model):
    title = models.CharField(blank=True, max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_url(self):
        return self.image.url

    def __str__(self):
        return self.title


class Protfolio_Category(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Protfolio(models.Model):
    title = models.CharField(blank=True, max_length=300)
    pro_category = models.ForeignKey(Protfolio_Category, on_delete=models.CASCADE)
    details = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(blank=True, max_length=300)
    details = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Experience_project(models.Model):
    work_category = models.CharField(max_length=150)
    place_name = models.CharField(max_length=250)
    work_year = models.CharField(max_length=10)
    details = models.TextField()

    def __str__(self):
        return self.work_category


# faq
class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
