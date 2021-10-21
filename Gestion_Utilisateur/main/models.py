from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    sexe = (
        ('Homme' , 'Homme'),
        ('Femme' , 'Femme'),
        ('Autre' , 'Autre'),
    )
    nom = models.CharField( "nom utilisateur", max_length=50)
    prenom = models.CharField("prénom utilisateur ", max_length=50)
    sexe = models.CharField( "genre utilisateur", max_length=10, choices=sexe)
    date_nais = models.DateField("Date de naissance", auto_now=False, auto_now_add=False)
    email = models.EmailField("Email", max_length=254)
    phone = models.CharField("Téléphone", max_length=50)
    photo = models.ImageField("photo de utilisateur", upload_to="media/")

    def __str__(self):
        return self.nom + '  ' + self.prenom
    