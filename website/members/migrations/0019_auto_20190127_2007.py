# Generated by Django 2.0.4 on 2019-01-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_auto_20190112_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(blank=True, help_text="Nick o sobrenombre, usar '-' para indicar que no se desea tener uno", max_length=317, null=True, verbose_name='nick'),
        ),
    ]
