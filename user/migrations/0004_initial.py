# Generated by Django 4.1.3 on 2022-12-16 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_remove_user_group_delete_group_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.group')),
            ],
        ),
    ]
