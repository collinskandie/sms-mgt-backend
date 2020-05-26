# Generated by Django 3.0.6 on 2020-05-26 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20200524_1220'),
        ('sms', '0007_auto_20200524_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Contact'),
        ),
    ]
