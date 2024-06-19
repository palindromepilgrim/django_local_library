# Generated by Django 5.0.6 on 2024-06-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(help_text='Enter language of book', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.ManyToManyField(to='catalog.language'),
        ),
    ]