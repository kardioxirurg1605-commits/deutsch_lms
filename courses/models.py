from django.db import models
from django.contrib.auth.models import User

# 1. Kapitel (Darslar) Modeli
class Chapter(models.Model):
    number = models.IntegerField(unique=True, verbose_name="Kapitel raqami") # 1, 2, ..., 12
    title = models.CharField(max_length=200, verbose_name="Dars mavzusi")   # "Guten Tag!"
    level = models.CharField(max_length=10, default="A1.1", verbose_name="Darajasi")
    grammar_content = models.TextField(help_text="Kursbuch dars nazariyasi (HTML formatida)")

    def __str__(self):
        return f"Kapitel {self.number}: {self.title}"

# 2. Uyga Vazifalar Modeli (Übungsbuch)
class Homework(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Tekshirilmadi'),
        ('graded', 'Tekshirildi'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="O'quvchi")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name="Qaysi Kapitel")
    submission_text = models.TextField(verbose_name="O'quvchi javobi")
    teacher_feedback = models.TextField(blank=True, null=True, verbose_name="O'qituvchi izohi")
    grade = models.IntegerField(blank=True, null=True, verbose_name="Baho (1-10)")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")

    def __str__(self):
        return f"{self.student.username} - Kapitel {self.chapter.number}"