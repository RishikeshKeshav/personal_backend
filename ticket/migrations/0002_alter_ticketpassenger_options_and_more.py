# Generated by Django 4.1.3 on 2022-11-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketpassenger',
            options={'verbose_name': 'Ticket Passenger', 'verbose_name_plural': 'Ticket Passengers'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('credit_card', 'credit_card')], default='credit_card', max_length=50),
        ),
    ]
