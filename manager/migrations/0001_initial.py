# Generated by Django 3.2.18 on 2023-06-25 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreePhotosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='tree_photos/')),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('tree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TreeInfoPhotos', to='app.treeinfomodel')),
            ],
        ),
        migrations.CreateModel(
            name='PersonPhotosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='person_photos/')),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.responsiblepersonmodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationPhotosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='organ_photos/')),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('organ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrganizationPhotos', to='app.organizationmodel')),
            ],
        ),
    ]
