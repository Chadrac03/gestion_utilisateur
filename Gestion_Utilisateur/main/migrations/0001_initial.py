# Generated by Django 3.2.8 on 2021-10-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='nom utilisateur')),
                ('prenom', models.CharField(max_length=50, verbose_name='prénom utilisateur ')),
                ('sexe', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autre', 'Autre')], max_length=10, verbose_name='genre utilisateur')),
                ('date_nais', models.DateField(verbose_name='Date de naissance')),
                ('Adresse', models.CharField(max_length=100, verbose_name='Adresse')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='Téléphone')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='photo de utilisateur')),
            ],
        ),
    ]
