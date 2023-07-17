from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'author']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            return super().save_model(request, obj, form, change)


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'parent', 'create_date', 'is_delete']


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
