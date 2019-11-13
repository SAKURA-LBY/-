from django.contrib import admin

# Register your models here.

from .models import book_bookinfo,book_heroinfo

admin.site.register(book_bookinfo)
admin.site.register(book_heroinfo)