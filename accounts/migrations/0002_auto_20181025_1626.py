# Generated by Django 2.1.2 on 2018-10-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolink',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='Дата публикации'),
        ),
    ]
