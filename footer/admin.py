from django.contrib import admin
from footer.models import FooterMeta, FooterContactMeta


class FooterMetaAdmin(admin.ModelAdmin):
    list_display = ['title', 'instagram']


class FooterContactMetaAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'address']


admin.site.register(FooterContactMeta, FooterContactMetaAdmin)
admin.site.register(FooterMeta, FooterMetaAdmin)
