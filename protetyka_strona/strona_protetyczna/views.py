from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CennikForm
from .models import CennikPozycja, OfertaPracy

def index(request):
    return render(request, 'strona_protetyczna/index.html')

def o_nas(request):
    return render(request, 'strona_protetyczna/o_nas.html')

def cennik(request):
    pozycje_cennika = CennikPozycja.objects.all()
    return render(request, 'strona_protetyczna/cennik.html', {'pozycje_cennika': pozycje_cennika})

def portfolio(request):
    return render(request, 'strona_protetyczna/portfolio.html')

def kontakt(request):
    return render(request, 'strona_protetyczna/kontakt.html')

def oferty_pracy(request):
    oferty = OfertaPracy.objects.filter(aktywna=True).order_by('-data_dodania')
    return render(request, 'strona_protetyczna/oferty_pracy.html', {'oferty': oferty})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('strona_glowna')
            else:
                form.add_error(None, 'Nieprawidłowa nazwa użytkownika lub hasło.')
    else:
        form = LoginForm()
    return render(request, 'strona_protetyczna/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('strona_glowna')

def register_view(request):
    # Tutaj możesz dodać logikę rejestracji, jeśli chcesz
    return render(request, 'strona_protetyczna/register.html')

@login_required
def dodaj_cennik(request):
    if request.method == 'POST':
        form = CennikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cennik')
    else:
        form = CennikForm()
    return render(request, 'strona_protetyczna/dodaj_cennik.html', {'form': form})

@login_required
def edytuj_cennik(request, pozycja_id):
    pozycja = get_object_or_404(CennikPozycja, pk=pozycja_id)
    if request.method == 'POST':
        form = CennikForm(request.POST, instance=pozycja)
        if form.is_valid():
            form.save()
            return redirect('cennik')
    else:
        form = CennikForm(instance=pozycja)
    return render(request, 'strona_protetyczna/edytuj_cennik.html', {'form': form, 'pozycja': pozycja})

@login_required
def usun_cennik(request, pozycja_id):
    pozycja = get_object_or_404(CennikPozycja, pk=pozycja_id)
    if request.method == 'POST':
        pozycja.delete()
        return redirect('cennik')
    else:
        return redirect('cennik')