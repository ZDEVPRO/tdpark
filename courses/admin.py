from django.contrib import admin
from courses.models import Courses, FeaturedCourse


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(FeaturedCourse)
admin.site.register(Courses, CoursesAdmin)
