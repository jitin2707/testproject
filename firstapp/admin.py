from django.contrib import admin


from firstapp.models import UserRole,SiteUser,NewSiteUser
# Register your models here.

admin.site.register(UserRole)
admin.site.register(SiteUser)
admin.site.register(NewSiteUser)