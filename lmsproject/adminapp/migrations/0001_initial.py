# Generated by Django 2.1 on 2023-09-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('bookid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('isbno', models.CharField(max_length=15)),
                ('program', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('bookname', models.CharField(max_length=100)),
                ('authorname', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.CharField(max_length=15)),
                ('isbno', models.CharField(max_length=15)),
                ('program', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('bookname', models.CharField(max_length=100)),
                ('authorname', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('issuedate', models.CharField(max_length=30)),
                ('duedate', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
