# Generated by Django 3.0.5 on 2020-05-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_delete_commentdeleteview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=250, verbose_name='comment text'),
        ),
    ]
