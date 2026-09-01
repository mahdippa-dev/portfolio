from projects.models import Project
from .models import About, SkillCategory, Skill, WorkStatus
from contact.forms import ContactMessageForm
from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse


# Create your views here.

def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /ckeditor5/

Sitemap: https://mahdippa.ir/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type='text/plain'
    )


def page_404(request, exception):
    return render(request, '404.html', status=404)


def page_500(request):
    return render(
        request,
        '500.html',
        status=500
    )


def home(request):
    about_me = About.objects.first()

    categories = SkillCategory.objects.order_by(
        'display_order'
    ).prefetch_related(
        Prefetch(
            'skills',
            queryset=Skill.objects.filter(
                displayStatus=True
            ).order_by('display_order')
        )
    )

    featured_projects = Project.objects.filter(
        is_featured=True
    ).order_by(
        'display_order'
    )

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            return JsonResponse({
                'success': True,
                'message': 'پیام شما با موفقیت ارسال شد.'
            })

        else:

            return JsonResponse({
                'success': False,
                'errors': form.errors
            })

    else:

        form = ContactMessageForm()
    workstatus = WorkStatus.objects.first()
    return render(request, 'core/home.html', {
        'about_me': about_me,
        'categories': categories,
        'featured_projects': featured_projects,
        'form': form,
        'work_status': workstatus
    })


def skills(request):
    categories = SkillCategory.objects.order_by(
        'display_order'
    ).prefetch_related(
        Prefetch(
            'skills',
            queryset=Skill.objects.filter(
                displayStatus=True
            ).order_by('display_order')
        )
    )

    return render(request, 'core/skills.html', {
        'categories': categories,
    })
