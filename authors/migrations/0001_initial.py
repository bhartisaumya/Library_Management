# Generated by Django 3.2.16 on 2022-12-18 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('usermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.usermodel')),
                ('description', models.CharField(max_length=450)),
            ],
            bases=('users.usermodel',),
        ),
    ]
