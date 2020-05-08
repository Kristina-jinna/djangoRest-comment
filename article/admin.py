from django.contrib import admin
from .models import UserAuthor,Group,Post
# Register your models here.

admin.site.register(UserAuthor)
admin.site.register(Group)
admin.site.register(Post)