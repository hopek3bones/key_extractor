from django.shortcuts import render
from django     import urls


def show_index(request):
    eg = """
Un réseau de télévision est un réseau de télécommunications destiné à la distribution de programmes télévisés. 
Cependant, le terme désigne désormais un groupement d'affiliés régionaux autour d'une chaîne de télévision 
centrale, offrant une programmation à plusieurs stations de télévision locales.

Jusqu'au milieu des années 1980, la programmation télévisée de la plupart des pays du monde a été 
dominée par un petit nombre de réseaux de diffusion. Bon nombre des premiers réseaux de télévision 
(comme la BBC, NBC ou CBS) se sont développés à partir de réseaux de radio existants.
"""
    return render(request, 'index.html', {"text": eg});


urlpatterns = [
    urls.path('', show_index, name="Home page"),
];
