from .models import Footer


def footer(request):
    footer_info = Footer.objects.first()

    return {
        'footer_info': footer_info
    }