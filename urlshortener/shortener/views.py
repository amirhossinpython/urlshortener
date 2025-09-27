import random, string
from django.shortcuts import render, redirect, get_object_or_404
from .models import Link



def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def home(request):
    new_url = None
    if request.method == "POST":
        original = request.POST.get("url")
        if original:
            code = generate_code()
            link = Link.objects.create(original_url=original, short_code=code)
            new_url = request.build_absolute_uri('/') + code + '/'
    return render(request, "home.html", {"new_url": new_url})


def redirect_link(request, code):
    link = get_object_or_404(Link, short_code=code)
    link.clicks += 1
    link.save()
    return redirect(link.original_url)
