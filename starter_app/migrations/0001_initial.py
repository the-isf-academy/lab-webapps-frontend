# Generated by Django 3.1.3 on 2021-03-29 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_assigned_to', models.CharField(blank=True, default='', max_length=30)),
                ('task_assigned_by', models.CharField(default='', editable=False, max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=8)),
                ('notes', models.TextField(max_length=200)),
                ('due_date', models.DateField(verbose_name='Date Due')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Created')),
                ('archive', models.BooleanField(default=False)),
                ('task_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
