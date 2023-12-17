# Generated by Django 5.0 on 2023-12-16 20:45

from django.db import migrations

def create_data(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    Post(Title="First Post", content="Content", topic = "Topic").save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [        migrations.RunPython(create_data),

    ]