from django.shortcuts import render, get_object_or_404

from projects.models import Project


# Create your views here.

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(request, 'projects/project_detail.html', {
        'project': project,
    })