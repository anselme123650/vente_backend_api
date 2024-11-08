# Generated by Django 5.1.2 on 2024-11-06 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bonCommande', '0001_initial'),
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.IntegerField()),
                ('bon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='bonCommande.boncommande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
    ]
