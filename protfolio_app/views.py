from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Footer_Header,About_me,Contact,project,Category,Service,Education,Skills,Protfolio_Category, \
    Protfolio,FAQ,Experience_project
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .form import Contact_Form
from django.core.mail import send_mail
from django.conf import settings
# download Cv
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound


# Create your views here.


def HomePage(request):
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)
    total_project = project.objects.order_by('-id')[:6]
    all_service = Service.objects.order_by('-id')[:6]
    education = Education.objects.all()
    Experience_proj = Experience_project.objects.all()
    Skill = Skills.objects.all()
    Resent_Skill = Skills.objects.order_by('-id')[:3]
    prot_category = Protfolio_Category.objects.order_by('-id')[:3]
    total_protfolio = Protfolio.objects.all()[:9]
    Faq = FAQ.objects.all()[:12]

    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            Message = form.cleaned_data.get('details')
            Contact.objects.create(name=name,email=email,subject=subject,Meassage=Message)
            from_email = form.cleaned_data.get('email')
            to_email = settings.EMAIL_HOST_USER
            to_list = [to_email]
            send_mail(subject,Message,from_email,to_list)

            return redirect('home')
        else:
            return redirect('home')
    else:
        form = Contact_Form()

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "total_project": total_project,
        "education": education,
        "all_service": all_service,
        "Skill": Skill,
        "Experience_proj": Experience_proj,
        "Resent_Skill": Resent_Skill,
        "prot_category": prot_category,
        "total_protfolio": total_protfolio,
        "Faq": Faq,
        "form": form,
    }
    return render(request,'index.html',data)


def Single_view(request,id):
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)
    single_post = get_object_or_404(project,id=id)
    resent_post = project.objects.all().order_by('-id')[:4]
    category = Category.objects.all()

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "single_post": single_post,
        "resent_post": resent_post,
        "category": category,
    }

    return render(request,'single_page.html',data)


def search(request):
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)

    try:
        q = request.POST.get('q')
    except:
        q = None
    if q:
        search_pro = project.objects.filter(title__icontains=q) | project.objects.filter(details__icontains=q)

        data = {
            "footer_Header": footer_header,
            "about_me": about_me,
            "search_product": search_pro,

        }
        return render(request,'search_product.html',data)

    else:
        data = {
        }
        return render(request,'Eorr_440.html',data)


def about_page(request):
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)
    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
    }
    return render(request,'total_single_page/about_page.html',data)


def Resume_page(request):
    education = Education.objects.all()
    Experience_proj = Experience_project.objects.all()
    Skill = Skills.objects.all()
    Resent_Skill = Skills.objects.order_by('-id')[:3]
    footer_header = get_object_or_404(Footer_Header)
    data = {
        "footer_Header": footer_header,
        "Experience_proj": Experience_proj,
        "education": education,
        "Skill": Skill,
        "Resent_Skill": Resent_Skill,
    }
    return render(request,'total_single_page/Resume_page.html',data)


def Services_page(request):
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)
    all_service = Service.objects.all()

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "all_service": all_service,
    }
    return render(request,'total_single_page/service_page.html',data)


def projects_page(request):
    total_project = project.objects.all()
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)
    page = request.GET.get('page',1)
    paginator = Paginator(total_project,3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        "total_project": users,
        "footer_Header": footer_header,
        "about_me": about_me,
    }
    return render(request,'total_single_page/project_page.html',data)


def Protfolio_page(request):
    total_project = project.objects.all()
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)
    prot_category = Protfolio_Category.objects.order_by('-id')[:3]
    total_protfolio = Protfolio.objects.all()
    data = {
        "total_project": total_project,
        "footer_Header": footer_header,
        "about_me": about_me,
        "prot_category": prot_category,
        "total_protfolio": total_protfolio,
    }
    return render(request,'total_single_page/protfolio_page.html',data)


def contact_page(request):
    total_project = project.objects.all()
    footer_header = get_object_or_404(Footer_Header)
    about_me = get_object_or_404(About_me)

    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            Message = form.cleaned_data.get('details')
            Contact.objects.create(name=name,email=email,subject=subject,Meassage=Message)

            return redirect('home')
        else:
            return redirect('home')
    else:
        form = Contact_Form()
    data = {
        "total_project": total_project,
        "footer_Header": footer_header,
        "about_me": about_me,
        "form": form,
    }
    return render(request,'total_single_page/contact_page.html',data)


# protfolio
def single_page_2View(request,id):
    footer_header = get_object_or_404(Footer_Header)
    single_protfolio = get_object_or_404(Protfolio,id=id)
    cate_protfolio = Protfolio_Category.objects.all()
    resen_protf = Protfolio.objects.order_by('-id')[:3]
    data = {
        "footer_Header": footer_header,
        "single_protfolio": single_protfolio,
        "cate_protfolio": cate_protfolio,
        "resen_protf": resen_protf,
    }
    return render(request,'single_page2.html',data)


def Protfolio_search(request):
    footer_header = get_object_or_404(Footer_Header)

    try:
        q = request.POST.get('q')
    except:
        q = None
    if q:
        search_pro_2 = Protfolio.objects.filter(title__icontains=q) | Protfolio.objects.filter(details__icontains=q)

        data = {
            "footer_Header": footer_header,
            "search_protfolio": search_pro_2,

        }
        return render(request,'search_protfolio.html',data)

    else:
        data = {
        }
        return render(request,'Eorr_440.html',data)


def download_pdf(request):
    # about_CV = get_object_or_404(About_me)
    # name=about_CV.cv.url
    fs = FileSystemStorage()
    filename = 'pdf_cv/atikur.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:

            response = HttpResponse(pdf,content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="atikur.pdf"'
            return response

    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
