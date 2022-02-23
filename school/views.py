from django.views.generic import ListView
from django.shortcuts import render
import json
from .models import Student

if not Student.teacher.all():
    with open('school.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        for student in data:
            if student['model'] == 'school.student':
                for entry in Student.objects.filter(name=student['fields']['name']):
                    entry.teacher.add(student['fields']['teacher'])


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    student_obj = Student.objects.order_by(ordering).prefetch_related('teacher')
    context = {
        'object_list': student_obj,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    return render(request, template, context)
