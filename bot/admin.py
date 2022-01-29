
from django.contrib import admin
from bot.models import contact,FAQ,Questions

@admin.register(FAQ)
class postAdmin(admin.ModelAdmin):
    list_display=['id','question']
    list_filter = ['pub_date']
    ordering=['id']
    search_fields = ['question']

@admin.register(Questions)
class postAdmin(admin.ModelAdmin):  
    list_display=['id','ask_query']
    list_filter = ['id']
    ordering=['id']
    search_fields = ['ask_query']
 

admin.site.register(contact)



#admin.site.register(FAQ)
#admin.site.register(Questions)
