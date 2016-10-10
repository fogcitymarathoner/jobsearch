from django.conf import settings
def static_url(request):
    return {'static_url': settings.STATIC_URL}

def media_url(request):
    return {'media_url': settings.MEDIA_URL}

def uri(request):
    return {'uri': settings.APP_URI}
