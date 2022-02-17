from django.contrib import admin
from blog.models import HomeBlog, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'image_tag', 'create_on_time', 'create_on_date']
    readonly_fields = ('id', 'image_tag', 'create_on_time', 'create_on_date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(HomeBlog)
admin.site.register(Blog, BlogAdmin)
