from django.core.mail import send_mail
from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import SkillHive, Lesson
from django.core.mail import EmailMultiAlternatives

def bio(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')

        subject = 'Новый Контакт В Базе'
        from_email = 'Skill Hive <skillhivecorp@gmail.com>'
        to_email = 'warkigarki@gmail.com'
        text_content = f'Имя: {name}\nТелефон: {phone}'
        html_content = f'<p><strong>Имя:</strong> {name}</p><p><strong>Телефон:</strong> {phone}</p>'

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        if request.user.is_authenticated:
            return redirect('/account')
        else:
            return render(request, 'bio.html')
    else:
        if request.user.is_authenticated:
            return redirect('/account')
        else:
            return render(request, 'bio.html')

def courses(request):
    courses = SkillHive.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(SkillHive, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'cour_id.html', {'course': course, 'lessons': lessons})
def lessons_detail(request, course_id, lessons_id):
    course = get_object_or_404(SkillHive, pk=course_id)
    lesson = get_object_or_404(Lesson, pk=lessons_id, course=course)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'lessons_id.html', {'course': course, 'lesson': lesson,'lessons':lessons})

