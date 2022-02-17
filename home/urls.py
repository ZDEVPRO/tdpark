from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('course/<int:id>/<slug:slug>', views.course_detail, name='course_details'),
    path('instructor/', views.instructor, name='instructor'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/<slug:slug>', views.blog_detail, name='blog_details'),
    path('contact/', views.contact, name='contact'),
]
