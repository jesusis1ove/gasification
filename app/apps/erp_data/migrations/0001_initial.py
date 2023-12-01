# Generated by Django 4.2.5 on 2023-11-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_house_number', models.CharField(blank=True, max_length=255, null=True)),
                ('address_city', models.CharField(blank=True, max_length=255, null=True)),
                ('address_locality', models.CharField(blank=True, max_length=255, null=True)),
                ('address_region', models.CharField(blank=True, max_length=255, null=True)),
                ('address_district', models.CharField(blank=True, max_length=255, null=True)),
                ('address_street', models.CharField(blank=True, max_length=255, null=True)),
                ('address_corps', models.CharField(blank=True, max_length=255, null=True)),
                ('address_apartment', models.IntegerField(blank=True, null=True)),
                ('bremin_code', models.CharField(blank=True, max_length=255, null=True)),
                ('counterparty_guid', models.CharField(blank=True, db_column='counterparty_GUID', max_length=255, null=True)),
                ('guid', models.CharField(blank=True, db_column='GUID', max_length=255, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'construction_objects',
            },
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('counterparty_head_guid', models.CharField(blank=True, db_column='counterparty_head_GUID', max_length=150, null=True)),
                ('counterparty_inn', models.CharField(blank=True, max_length=12, null=True)),
                ('is_archived', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('fullname', models.TextField(blank=True, null=True)),
                ('bank_account_guid', models.CharField(blank=True, db_column='bank_account_GUID', max_length=150, null=True)),
                ('contract_guid', models.CharField(blank=True, db_column='contract_GUID', max_length=150, null=True)),
                ('guid', models.CharField(blank=True, db_column='GUID', max_length=150, null=True, unique=True)),
                ('counterparty_type', models.CharField(blank=True, max_length=150, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'counterparties',
            },
        ),
        migrations.CreateModel(
            name='CounterpartyOrder',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('accepted_date', models.DateTimeField(blank=True, null=True)),
                ('departure_date', models.DateTimeField(blank=True, null=True)),
                ('counterparty_name', models.CharField(blank=True, max_length=255, null=True)),
                ('manager_guid', models.CharField(blank=True, db_column='manager_GUID', max_length=255, null=True)),
                ('employe_name', models.CharField(max_length=255)),
                ('temp_order_id', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.CharField(max_length=255)),
                ('counterparty_guid', models.CharField(db_column='counterparty_GUID', max_length=255)),
                ('construction_object_guid', models.CharField(blank=True, db_column='construction_object_GUID', max_length=150, null=True)),
                ('order_type_id', models.IntegerField()),
                ('bremin_code', models.CharField(blank=True, max_length=255, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'counterparty_orders',
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('bremin_code', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'order_types',
            },
        ),
        migrations.CreateModel(
            name='WorkPackage',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('work_package', models.CharField(blank=True, max_length=150, null=True)),
                ('construct_object_guid', models.CharField(blank=True, db_column='construct_object_GUID', max_length=150, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'work_packages',
            },
        ),
    ]