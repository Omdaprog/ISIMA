# Generated by Django 3.1 on 2020-09-27 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isima_trivez', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfstore',
            name='image',
        ),
        migrations.CreateModel(
            name='PdfImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isima_trivez.pdfstore')),
            ],
        ),
    ]
