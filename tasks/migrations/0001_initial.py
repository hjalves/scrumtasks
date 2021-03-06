# Generated by Django 2.0.1 on 2018-01-21 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('D', 'Done'), ('O', 'Doing')], default='D', max_length=1)),
                ('time_spent', models.DurationField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlannedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('redmine', models.CharField(max_length=100)),
                ('gitlab', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('entry', models.DateTimeField(blank=True, null=True)),
                ('working_time', models.DurationField(blank=True, null=True)),
                ('breaks', models.DurationField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='plannedtask',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.Project'),
        ),
        migrations.AddField(
            model_name='plannedtask',
            name='working_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_tasks', to='tasks.WorkingDay'),
        ),
        migrations.AddField(
            model_name='executedtask',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.Project'),
        ),
        migrations.AddField(
            model_name='executedtask',
            name='working_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executed_tasks', to='tasks.WorkingDay'),
        ),
    ]
