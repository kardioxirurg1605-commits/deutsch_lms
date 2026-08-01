from django.shortcuts import render, get_object_or_404
from .models import Chapter, Homework

def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    success = False

    if request.method == 'POST':
        submission_text = request.POST.get('submission')
        # Agar foydalanuvchi tizimga kirgan bo'lsa uni olamiz, bo'lmasa birinchi adminni biriktiramiz
        student = request.user if request.user.is_authenticated else None
        
        if student:
            Homework.objects.create(
                student=student,
                chapter=chapter,
                submission_text=submission_text
            )
            success = True

    return render(request, 'courses/chapter_detail.html', {
        'chapter': chapter,
        'success': success
    })
    from django.shortcuts import render, get_object_or_404
from .models import Chapter, Homework

# 1. Barcha darslar ro'yxati (Bosh sahifa)
def chapter_list(request):
    chapters = Chapter.objects.all().order_by('number')
    return render(request, 'courses/chapter_list.html', {'chapters': chapters})

# 2. Bitta darsning ichki sahifasi
def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    success = False

    if request.method == 'POST':
        submission_text = request.POST.get('submission')
        student = request.user if request.user.is_authenticated else None
        
        if student:
            Homework.objects.create(
                student=student,
                chapter=chapter,
                submission_text=submission_text
            )
            success = True

    return render(request, 'courses/chapter_detail.html', {
        'chapter': chapter,
        'success': success
    })