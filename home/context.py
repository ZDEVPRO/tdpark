from home.models import HeaderLogo, HomeTitle, AboutSection, Total, Teacher
from courses.models import Courses, FeaturedCourse
from footer.models import FooterMeta, FooterContactMeta
from blog.models import Blog, HomeBlog


def footermetaview(request):
    footer_meta_latest = FooterMeta.objects.all().order_by('-id')[:1]
    context = {
        'footer_meta_latest': footer_meta_latest,
    }
    return context


def featuredcourseview(request):
    featured_course_latest = FeaturedCourse.objects.all().order_by('-id')[:3]
    context = {
        'featured_course_latest': featured_course_latest,
    }
    return context


def homeblogview(request):
    home_blog_latest = HomeBlog.objects.all().order_by('-id')[:3]
    context = {
        'home_blog_latest': home_blog_latest,
    }
    return context


def headerlogoview(request):
    logo_header_latest = HeaderLogo.objects.all().order_by('-id')[:1]
    context = {
        'logo_header_latest': logo_header_latest,
    }
    return context


def totalview(request):
    total_latest = Total.objects.all().order_by('-id')[:1]
    context = {
        'total_latest': total_latest,
    }
    return context


def teacherview(request):
    teacher_latest = Teacher.objects.all().order_by('-id')[:20]
    context = {
        'teacher_latest': teacher_latest,
    }
    return context


def blogview(request):
    blog_latest = Blog.objects.all().order_by('-id')[:20]
    context = {
        'blog_latest': blog_latest,
    }
    return context


def aboutsectionview(request):
    about_section_latest = AboutSection.objects.all().order_by('-id')[:1]
    context = {
        'about_section_latest': about_section_latest,
    }
    return context


def hometitleview(request):
    home_title_latest = HomeTitle.objects.all().order_by('-id')[:1]
    context = {
        'home_title_latest': home_title_latest,
    }
    return context


def coursesview(request):
    courses_latest = Courses.objects.all().order_by('-id')[:30]
    context = {
        'courses_latest': courses_latest,
    }
    return context


def footercontactmetaview(request):
    footer_contact_meta = FooterContactMeta.objects.all().order_by('-id')[:1]
    context = {
        'footer_contact_meta': footer_contact_meta,
    }
    return context
