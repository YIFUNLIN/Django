from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')   #讓網頁版Django 可以多顯示其他欄位資訊

admin.site.register(Post,PostAdmin)    #讓網頁版Django 可以多顯示其他欄位資訊