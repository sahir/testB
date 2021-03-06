# Generated by Django 2.0.8 on 2020-04-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generatefaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Businesses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('loyalty_program_type', models.CharField(blank=True, max_length=255, null=True)),
                ('preferences', models.CharField(blank=True, max_length=255, null=True)),
                ('stage', models.CharField(blank=True, max_length=255, null=True)),
                ('restaurant_type', models.CharField(blank=True, max_length=255, null=True)),
                ('uuid', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'businesses',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='ReceiptMessages',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('business_id', models.IntegerField()),
                ('line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('line_3', models.CharField(blank=True, max_length=255, null=True)),
                ('line_4', models.CharField(blank=True, max_length=255, null=True)),
                ('line_5', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('header', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'receipt_messages',
            },
        ),
        migrations.AlterModelOptions(
            name='locationkeys',
            options={},
        ),
    ]
