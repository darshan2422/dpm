# Generated by Django 2.2.2 on 2019-06-22 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentname', models.CharField(help_text='Student Name', max_length=100, null=True)),
                ('Branch', models.CharField(help_text='Branch', max_length=50, null=True)),
                ('IssueDate', models.DateField(default=datetime.date.today, verbose_name='Issued')),
                ('SubmissionDate', models.DateField(null=True, verbose_name='Submission')),
                ('IssuedBooks', models.IntegerField(help_text='BooksIssued', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]