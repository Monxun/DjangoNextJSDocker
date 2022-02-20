# Generated by Django 3.2.6 on 2021-09-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(default='John Doe', max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]