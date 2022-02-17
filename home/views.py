from courses.models import Courses
from django.shortcuts import render, redirect
from home.forms import AloqaForm
from home.models import AloqaModel
from django.contrib import messages
from blog.models import Blog


def index(request):
    return render(request, 'index/base.html')


def about(request):
    return render(request, 'about/base.html')


def courses(request):
    return render(request, 'courses/base.html')


def instructor(request):
    return render(request, 'instructor/base.html')


def contact(request):
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            data = AloqaModel()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()  # save data to table
            messages.success(request, "Xurmatli sayt adminstratori sizga yangi xabar keldi.")
            return redirect('contact')

    form = AloqaForm

    context = {
        'form': form,
    }
    return render(request, 'contact/base.html', context)


def blogview(request):
    blog_latest = Blog.objects.all().order_by('-id')[:20]
    context = {
        'blog_latest': blog_latest,
    }
    return render(request, 'blog/base.html', context)


def blog(request):
    return render(request, 'blog/base.html')


def course_detail(request, id, slug):
    courses_latest = Courses.objects.all().order_by('-id')
    course = Courses.objects.get(pk=id)
    context = {
        'course': course,
        'courses_latest': courses_latest,
    }
    return render(request, 'course_details/base.html', context)


def blog_detail(request, id, slug):
    blog_latest = Blog.objects.all().order_by('-id')
    blogs = Blog.objects.get(pk=id)
    context = {
        'blogs': blogs,
        'blog_latest': blog_latest,
    }
    return render(request, 'blog_details/base.html', context)
