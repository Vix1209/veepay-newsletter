
from django.contrib import admin
from .models import Newsletter #, MailMessage

#To unregister a model. E.G The default models given to us by django at the admin site
#from django.contrib.auth.models import Group
# admin.site.unregister(Group) 

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    
# Register your models here.

admin.site.register(Newsletter, NewsletterAdmin)
# admin.site.register(MailMessage)


#To change the title of your admin page
admin.site.site_header = 'Veepay Telecommunications'

