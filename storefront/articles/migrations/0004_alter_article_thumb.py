# Generated by Django 3.2.10 on 2021-12-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='/article.png', upload_to=''),
        ),
    ]