# Generated by Django 4.1.3 on 2022-11-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_remove_ticket_passengers_ticketpassenger_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='passengers',
            field=models.ManyToManyField(related_name='passengers', to='ticket.ticketpassenger'),
        ),
    ]
