import pyshorteners
from django.shortcuts import render
from django.http import HttpResponse

def url_converter(request):
    if request.method == "POST":
        long_url = request.POST.get('long_url')
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        print(f'url shorted: {short_url}')
        context = {'short_url': short_url}
        return render(request, 'urlconverter/url_converted.html', context)
    return render(request, 'urlconverter/index.html')
