from django.contrib import admin

from .models import Post , Comment


class CommentAdminInLine(admin.TabularInline):
    model = Comment
    field = ["text"]
    extra = 0
    
"""به جای اون رجیستر که تو خط بیستم داریم میشه اینجا از قطعه کد زیر استفاذه کرد:
@admin.register(post)"""

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_enable", "created_time"]
    inlines = [CommentAdminInLine, ]

#class CommentAdmin(admin.ModelAdmin):
#    list_display = ["post", "text", "created_time"]
admin.site.register(Post, PostAdmin)
#admin.site.register(Comment, CommentAdmin)
