# Generated by Django 4.1.5 on 2023-01-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='ord_no',
            new_name='ordno',
        ),
    ]
