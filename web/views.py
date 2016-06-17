import os

from django.shortcuts import render
from django.http import HttpResponse
from .forms import *



def sellinglist(request):
        form = NameForm()

        print(request)
        if request.method == 'POST':
                form = NameForm(request.POST)
                if form.is_valid():
                        print(request.POST)



        return render(request, 'page.html', {'form': form})


def scripts(request, name):
        data = open(os.path.join('scripts', name), 'rb').read()

        return HttpResponse(data)
