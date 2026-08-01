from django.contrib import admin
from .models import Chapter, Homework

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'level')
    ordering = ('number',)

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('student', 'chapter', 'status', 'grade', 'created_at')
    list_filter = ('status', 'chapter')
    search_fields = ('student__username', 'submission_text')