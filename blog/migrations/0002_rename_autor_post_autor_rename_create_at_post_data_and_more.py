# Generated by Django 4.1.2 on 2022-10-21 23:23

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='Autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='Data',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='resumo',
            new_name='Titulo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='conteudo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Resumo',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Conteudo',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
