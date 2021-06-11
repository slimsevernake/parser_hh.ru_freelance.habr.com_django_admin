# Generated by Django 3.0.2 on 2021-06-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djadminka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacanci_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField(verbose_name='Название')),
                ('Link', models.URLField(verbose_name='Ссылка на вакансию')),
                ('Price', models.TextField(verbose_name='Зарплата')),
                ('Number_of_otkliks', models.TextField(verbose_name='Количество откликов')),
                ('Number_of_vues', models.TextField(verbose_name='Количество просмотров другими пользователями')),
            ],
            options={
                'verbose_name': 'Вакансии_2',
                'verbose_name_plural': 'Вакансии_2',
            },
        ),
        migrations.AlterModelOptions(
            name='vacanci',
            options={'verbose_name': 'Вакансии', 'verbose_name_plural': 'Вакансии'},
        ),
    ]