from django.conf import settings
from django.core.files.storage import FileSystemStorage
# from django.core.mail import BadHeaderError, send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (HttpResponse, HttpResponseNotFound,)
from django.shortcuts import (Http404, HttpResponse, get_object_or_404,
                              redirect, render)
# download Cv
from django.views.generic import View

from .form import Contact_Form
from .models import (FAQ, About_me, Contact, Education, Experience_project,
                     Footer_Header, Project_Category, Protfolio,
                     Protfolio_Category, Service, Skills, project)

# atiqur5
# Create your views here.


def HomePage(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.last()

    try:
        about_me = get_object_or_404(About_me).last()
    except:
        about_me = About_me.objects.last()

    total_project = project.objects.order_by('-id')[:6]  # for  index.html
    all_service = Service.objects.order_by('-id')[:6]  # for  index.html
    education = Education.objects.all().order_by('-id')
    Experience_proj = Experience_project.objects.all().order_by('-id')
    Skill = Skills.objects.all().order_by('id')[:6]
    Resent_Skill = Skills.objects.order_by('-id')[:3]
    port_category = Protfolio_Category.objects.order_by('-id')[:3]
    total_portfolio = Protfolio.objects.all().order_by('-id')[:9]
    Faq = FAQ.objects.all()[:12]

    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            Message = form.cleaned_data.get('details')
            Contact.objects.create(name=name, email=email, subject=subject, Meassage=Message)

            # from_email = form.cleaned_data.get('email')

            # body = {
            #     'first_name': form.cleaned_data['name'],
            #     'email': form.cleaned_data['email'],
            #     'details': form.cleaned_data['details'],
            # }
            # message = "\n".join(body.values())
            # to_email = settings.EMAIL_HOST_USER

            # recipient_list = [to_email,]
         
            # try:
            #     send_mail(subject, message, from_email, recipient_list , fail_silently=False)
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')

            return redirect('home')
        else:
            return redirect('home')
    else:
        form = Contact_Form()

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "education": education,
        "all_service": all_service,
        "Skill": Skill,
        "Experience_proj": Experience_proj,
        "Resent_Skill": Resent_Skill,
        "total_project": total_project,  # same name hobe projects_page def a
        "portfolio_cate": port_category,  # same name hobe Portfolio_page def a
        "total_portfolio": total_portfolio,  # same name hobe Portfolio_page def a
        "Faq": Faq,
        "form": form,
    }
    return render(request, 'index.html', data)


def projects_page(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')
    # because footer+about are both footer data

    total_project = project.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(total_project, 3)
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
    return render(request, 'total_single_page/project_page.html', data)  # because  total_single_page/project_page.html
    # dui ta def er jonno akta niyechi html page niyechi tai
    # page are user both def (projects_page and HomePage)


def Project_details_views(request, id):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')
    # because footer+about are both footer data (inheritance)

    single_project_post = get_object_or_404(project, id=id)
    project_resent_post = project.objects.all().order_by('-id')[:4]
    project_category = Project_Category.objects.all().order_by('-id')[:15]

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "single_post": single_project_post,
        "resent_post": project_resent_post,
        "project_category": project_category,
    }

    return render(request, 'project_details.html', data)


def project_search(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')

    # because footer+about are both footer data (inheritance)

    try:
        q = request.POST.get('project_search')
    except:
        q = None

    if q:
        search_pro = project.objects.filter(title__icontains=q) | project.objects.filter(details__icontains=q)
        data = {
            "footer_Header": footer_header,
            "about_me": about_me,
            "search_product": search_pro,
        }
        if search_pro.exists():
            return render(request, 'search_product.html', data)
        else:
            return render(request, 'search_not_found.html')

    else:
        data = {
            "footer_Header": footer_header,
            "about_me": about_me,

        }
        return render(request, 'Error-404.html', data)


def All_category_project_show(request, id):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')

    # because footer+about are both footer data (inheritance)

    pro_cat = get_object_or_404(Project_Category, id=id)
    project_all_category = project.objects.filter(category=pro_cat.id)

    page = request.GET.get('page', 1)
    paginator = Paginator(project_all_category, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "pro_cat": pro_cat,  # for category show
        "project_all_category": users,
    }

    if project_all_category.exists():
        return render(request, 'project_all_category_show.html', data)
    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
    }
    return render(request, 'project_category_Not_show.html', data)


def Portfolio_page(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')

    # because footer+about are both footer data (inheritance)

    portfolio_category = Protfolio_Category.objects.all().order_by('-id')[:3]
    total_portfolio = Protfolio.objects.all().order_by('-id')[:20]
    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "portfolio_cate": portfolio_category,  # HomePage(views def )portfolio_cate er name same
        "total_portfolio": total_portfolio,  # HomePage(views def ) portfolio_cate er name same
    }
    return render(request, 'total_single_page/portfolio_page.html',
                  data)  # because  total_single_page/portfolio_page.html
    # dui ta def er jonno akta niyechi html page niyechi tai
    # page are user both def (Portfolio_page and HomePage)


def portfolio_details_View(request, id):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    # try:
    #     about_me = get_object_or_404(About_me)
    # except:
    #     about_me = About_me.objects.latest('id')
    single_portfolio = get_object_or_404(Protfolio, id=id)
    category_portfolio = Protfolio_Category.objects.all()
    resen_protf = Protfolio.objects.order_by('-id')[:3]
    data = {
        "footer_Header": footer_header,
        "single_protfolio": single_portfolio,
        "category_portfolio": category_portfolio,
        "resen_protf": resen_protf,
    }
    return render(request, 'portfolio_details.html', data)


def Portfolio_search(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        q = request.POST.get('portfolio_search')
    except:
        q = None
    if q:
        portfolio_sear = Protfolio.objects.filter(title__icontains=q) | Protfolio.objects.filter(details__icontains=q)

        data = {
            "footer_Header": footer_header,
            "all_search_portfolio_show": portfolio_sear,

        }
        if portfolio_sear.exists():
            return render(request, 'search_protfolio.html', data)
        else:
            return render(request, 'search_not_found.html')


    else:
        data = {
            "footer_Header": footer_header,
        }
        return render(request, 'Error-404.html', data)


def about_page(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
    }
    return render(request, 'total_single_page/about_page.html', data)


def Resume_page(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    education = Education.objects.all()
    Experience_proj = Experience_project.objects.all()
    Skill = Skills.objects.all().order_by('id')[:6]
    Resent_Skill = Skills.objects.order_by('-id')[:3]
    data = {
        "footer_Header": footer_header,
        "Experience_proj": Experience_proj,
        "education": education,
        "Skill": Skill,
        "Resent_Skill": Resent_Skill,
    }
    return render(request, 'total_single_page/Resume_page.html', data)


def Services_page(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')

    all_service = Service.objects.all()

    data = {
        "footer_Header": footer_header,
        "about_me": about_me,
        "all_service": all_service,
    }
    return render(request, 'total_single_page/service_page.html', data)


def contact_page(request):
    try:
        footer_header = get_object_or_404(Footer_Header)
    except:
        footer_header = Footer_Header.objects.latest('id')

    try:
        about_me = get_object_or_404(About_me)
    except:
        about_me = About_me.objects.latest('id')

    total_project = project.objects.all()

    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            Message = form.cleaned_data.get('details')
            Contact.objects.create(name=name, email=email, subject=subject, Meassage=Message)
            from_email = form.cleaned_data.get('email')
            to_email = settings.EMAIL_HOST_USER
            to_list = [to_email]
            # send_mail(subject, Message, from_email, to_list)

            return redirect('home')
        else:
            return redirect('contact')
    else:
        form = Contact_Form()

    data = {
        "total_project": total_project,
        "footer_Header": footer_header,
        "about_me": about_me,
        "form": form,
    }
    return render(request, 'total_single_page/contact_page.html', data)


def download_pdf(request):
    pdf=About_me.objects.last()
    pdf_name=pdf.cv.name
 
    fs = FileSystemStorage()
    filename =pdf_name
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="atikur.pdf"' #user will be prompted with the browser’s open/save file
            response['Content-Disposition'] = 'inline; filename="atiqurCV'  # user will be prompted
            return response


    else:
        return HttpResponseNotFound('The requested pdf was not found in our server !.')
