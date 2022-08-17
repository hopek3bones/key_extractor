from django import urls
from rest_framework import decorators
from rest_framework import response
import kyxo as kx


# init NLP mdoel
kx.init(kx.FR_MODEL, kx.FR_ALPHA);


@decorators.api_view(['POST'])
def extract_keyword(request):
    text    = request.data.get('text');
    results = kx.get_keywords(text);
    return response.Response({'results': results}, status=200);


urlpatterns = [
    urls.path('get/keywords/', extract_keyword, name="keywords extraction"),
];
    
