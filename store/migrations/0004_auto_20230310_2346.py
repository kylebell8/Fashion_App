# Generated by Django 3.2.18 on 2023-03-10 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_producttest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.producttest'),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
