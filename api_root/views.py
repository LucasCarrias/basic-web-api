from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .utils import list_urls


@api_view(['GET'])
def api_url_list_view(request):
    urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])
    urls = dict()

    for url in list_urls(urlconf.urlpatterns):
        url = ''.join(url)
        if 'admin' in url:
            continue
        prefix = url.split('/')[0]

        url = "/".join([request.get_host(), url])

        if urls.get(prefix):
            urls[prefix].append(url)
        else:
            urls[prefix] = [url]

    return Response(urls)


