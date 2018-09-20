# Generated by Django 2.1.1 on 2018-09-19 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_account_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.Classroom'),
        ),
        migrations.AddField(
            model_name='student',
            name='firstName',
            field=models.CharField(default='first', max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='lastName',
            field=models.CharField(default='last', max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='studentNumber',
            field=models.CharField(default='0123456789', max_length=20),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
