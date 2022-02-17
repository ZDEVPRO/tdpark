from django.contrib import admin
from home.models import HeaderLogo, HomeTitle, AboutSection, Total, Teacher, AloqaModel


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'phone', 'image_tag']
    readonly_fields = ('image_tag',)


class HeaderLogoAdmin(admin.ModelAdmin):
    list_display = ['image_tag']
    readonly_fields = ('image_tag',)


class HomeTitleAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title']


class TotalAdmin(admin.ModelAdmin):
    list_display = ['num1', 'num2', 'num3', 'num4']


class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'button']


class AloqaAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'create_time', 'create_date']
    readonly_fields = ['message', 'name', 'subject', 'phone', 'create_time', 'create_date']


admin.site.register(AloqaModel, AloqaAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Total, TotalAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(HomeTitle, HomeTitleAdmin)
admin.site.register(HeaderLogo, HeaderLogoAdmin)
