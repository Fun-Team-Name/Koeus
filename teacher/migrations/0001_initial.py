# Generated by Django 2.1.1 on 2018-10-03 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(default='', max_length=40)),
                ('lastName', models.CharField(default='', max_length=40)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('name', models.CharField(default='Classroom', max_length=40)),
                ('key', models.CharField(default='Classroom', max_length=200, primary_key=True, serialize=False, unique=True)),
                ('teacher', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name', 'key'),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=40)),
                ('lastName', models.CharField(default='', max_length=40)),
                ('studentNumber', models.CharField(default='12345', max_length=20)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Classroom')),
            ],
            options={
                'ordering': ('lastName', 'firstName', 'studentNumber'),
            },
        ),
    ]