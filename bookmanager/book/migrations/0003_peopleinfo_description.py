# Generated by Django 2.2.5 on 2022-04-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220425_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='描述信息'),
        ),
    ]
