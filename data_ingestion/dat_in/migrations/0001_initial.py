# Generated by Django 2.1.5 on 2019-01-28 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100, null=True)),
                ('last_name', models.CharField(default='', max_length=100, null=True)),
                ('street_address', models.CharField(default='', max_length=100, null=True)),
                ('state', models.CharField(default='', max_length=100, null=True)),
                ('zip_code', models.CharField(default='', max_length=100, null=True)),
                ('date_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(null=True)),
                ('purchase_status', models.CharField(default='', max_length=8, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dat_in.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(null=True)),
                ('product_name', models.CharField(default='', max_length=100, null=True)),
                ('purchase_amount', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='purchasetype',
            unique_together={('product_id', 'product_name', 'purchase_amount')},
        ),
        migrations.AddField(
            model_name='orderrecord',
            name='purchase_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dat_in.PurchaseType'),
        ),
    ]
