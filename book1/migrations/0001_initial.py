# Generated by Django 2.1.5 on 2019-06-10 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Auther_info',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
                ('telephone', models.BigIntegerField()),
                ('addr', models.CharField(max_length=86)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('authers', models.ManyToManyField(to='book1.Auther')),
            ],
        ),
        migrations.CreateModel(
            name='Public_info',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='public',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book1.Public_info'),
        ),
        migrations.AddField(
            model_name='auther',
            name='authorinfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book1.Auther_info'),
        ),
    ]