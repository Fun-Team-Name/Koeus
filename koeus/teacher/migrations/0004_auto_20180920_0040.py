# Generated by Django 2.1.1 on 2018-09-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20180919_2353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('lastName', 'firstName', 'studentNumber')},
        ),
        migrations.AddField(
            model_name='classroom',
            name='name',
            field=models.CharField(default='Classroom', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstName',
            field=models.CharField(default='N/A', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(default='N/A', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentNumber',
            field=models.CharField(default='12345', max_length=20),
        ),
    ]