# Generated by Django 3.1.7 on 2021-04-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0006_autor_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
