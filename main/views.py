from django.contrib   import messages
from django.shortcuts import render
from django     import urls
import kyxo as kx


# init NLP mdoel
kx.init(kx.FR_MODEL, kx.FR_ALPHA);


def show_index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {"text": "", "ratio": 1.5});
    elif request.method == 'POST':
        text    = request.POST.get("text");
        ratio   = request.POST.get("ratio", 1.5);
        results = {};
        if text:
            print(text);
            results = kx.get_keywords(text, float(ratio));
            messages.success(request, "{} keyword(s) are extracted successfully!".format(len(results)));
        else: messages.warning(request, "Copy and paste any text in the textarea please.");
        return render(request, 'index.html', {"text": text, 'results': results, "ratio": ratio});


urlpatterns = [
    urls.path('', show_index, name="Home page"),
];
