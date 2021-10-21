from django.shortcuts import render , redirect , resolve_url
from django.http import HttpResponse 
from main.models import Utilisateur
from main.forms import Userform

# Create your views here.
def home(request) :
    return render(request, "main/index.html" , locals() )

def lister(request):
    user = Utilisateur.objects.all()
    return render(request, "main/liste.html" , locals() )

def create(request):
    """ Creation d'un nouveau Utilisateur"""
    
    data = request.POST
    photo = request.FILES['photo']

    us = Utilisateur.objects.create(
        nom = data.get('nom'),
        prenom = data.get('prenom'),
        sexe = data.get('sexe'),
        date_nais = data.get('date'),
        email= data.get('email'),
        phone = data.get('phone'),
        photo = photo,
    )
    us.save()

    return redirect(home)

def supprimer(request):
    
    data = request.POST
    if request.method == 'POST':
        id = data.get('ID')

    eleve_sup = Utilisateur.objects.get(id=id)
    eleve_sup.delete()
    return redirect(home)
    
def modifier(request, id):
    import base64
    data = request.POST
    photo = request.FILES
    user = Utilisateur.objects.get(id=id)

    if request.method == 'POST':
        user.nom = data.get('nom', user.nom)
        user.prenom = data.get('prenom', user.prenom)
        user.sexe = data.get('sexe', user.sexe)
        user.date_nais = data.get('date', user.date_nais)
        user.email = data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.photo = photo.get('photo', user.photo)
        
        user.save()
        return redirect(home)

    else :
        mod = True
        return render(request, 'main/enregistrer.html', locals())

def enregistrer(request):
    mod = False
    return render(request, 'main/enregistrer.html', locals())
