# Generated by Django 3.2.12 on 2022-03-18 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_marque', models.CharField(max_length=100)),
                ('lien_photo_marque', models.CharField(max_length=1000)),
                ('description_marque', models.CharField(max_length=2000)),
                ('nombre_votes_marque', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Boisson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_boisson', models.CharField(max_length=200)),
                ('lien_photo_boisson', models.CharField(max_length=1000)),
                ('description_boisson', models.CharField(max_length=2000)),
                ('nombre_votes_boisson', models.IntegerField(default=0)),
                ('marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.marque')),
            ],
        ),
    ]
