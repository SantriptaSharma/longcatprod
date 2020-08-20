from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages
from .models import ExtendedLink

# Create your views here.
def homepage(req):
    return render(req, "index.html")

def extendlink(req):
    badReq = False
    if req.method == "POST":
        segms = 0
        try:
            segms = int(req.POST["segments"])
        except:
            badReq = True
        
        if segms <= 0 or segms > 50:
            segms = 1
        
        ll = req.POST["link"]
        ll.replace(" ", "-")

        if(ExtendedLink.objects.all().filter(longlink = ll).count() != 0):
            messages.add_message(req, 20, "already exists")
        else:
            ExtendedLink.objects.create(url = req.POST["url"], longlink = ll, segments = segms)
            messages.add_message(req, 20, f"successfully created http://long-cat.herokuapp.com/{ll}")
    else:
        badReq = True

    if badReq:
        return HttpResponseBadRequest()
    else:
        return redirect("linkextender:index")

def longlink(req, longlink):
    get_object_or_404(ExtendedLink, longlink = longlink)
    return render(req, "head.html")

def longlinkseg(req, longlink, segno):
    elink = get_object_or_404(ExtendedLink, longlink=longlink)
    if(elink.segments == segno):
        return render(req, "tail.html", {"link": elink.url})
    else:
        return render(req, "segment.html", {"head": False, "segno": segno})
