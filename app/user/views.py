from django.shortcuts import render, redirect

from .forms import NewUserForm

from django.contrib.auth import login
from django.contrib import messages

def register_request(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.sucess(request, "Registrado com sucesso!")
            return redirect("main:homapage")
        else:
            messages.error(request, "Deu erro, baby!")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})
    