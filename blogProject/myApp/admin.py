from django.contrib import admin
from myApp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    l=['title','slug','author','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','created','publish','author')
    search_fields=['title','body']
    raw_id_fields=('author',)
    ordering=['status','publish']

admin.site.register(Post,PostAdmin)