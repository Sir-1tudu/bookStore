# Generated by Django 4.2.2 on 2023-07-03 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.users'))),
                ('Product_name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('Cart', models.TextField()),
                ('password', models.IntegerField()),
                ('confPassword', models.IntegerField()),
                ('usr_image', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Call',
        ),
    ]
