from django.shortcuts import render, redirect
from django.views import generic

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html', {
            "title": "heroku"
        })