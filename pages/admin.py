from django.contrib import admin
from pages.models import Post, Comment, Student, Course, Enrollment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'body','created_at')
    search_fields = ('title', "body")
    list_filter = ('created_at',)
    ordering = ("-created_at",)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author', 'text')
    list_filter = ('created_at',)


# @admin.register(Student)
# @admin.register(Course)
# @admin.register(Enrollment)



# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Student)
# admin.site.register(Course)
# admin.site.register(Enrollment)