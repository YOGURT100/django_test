from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {"title": "Home - главная", "content": "Магазин мебели HOME"}

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Lorem ipsum, dolor sit amet consectetur adipisicing elit.",
    }

    return render(request, "main/about.html", context)
