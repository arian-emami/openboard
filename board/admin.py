from django.contrib import admin

from .models import Board, IndexPage, Post, Reply, Tag

# Register your models here.
admin.site.register(Board)
admin.site.register(IndexPage)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Reply)
