# Generated by Django 3.0.6 on 2022-02-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('postdate', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='samplemodel',
            name='number',
        ),
    ]
