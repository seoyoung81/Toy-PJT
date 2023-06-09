# Generated by Django 3.2.13 on 2023-05-11 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('album_path', models.TextField()),
                ('tracks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('lyrics', models.TextField()),
                ('running_time', models.TimeField()),
                ('composer', models.CharField(max_length=30)),
                ('lyricist', models.CharField(max_length=30)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rockstars.album')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contemt', models.TextField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rockstars.band')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='bands',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rockstars.band'),
        ),
    ]
