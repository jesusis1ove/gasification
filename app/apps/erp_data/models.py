# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class ConstructionObject(models.Model):
    address_house_number = models.CharField(max_length=255, blank=True, null=True)
    address_city = models.CharField(max_length=255, blank=True, null=True)
    address_locality = models.CharField(max_length=255, blank=True, null=True)
    address_region = models.CharField(max_length=255, blank=True, null=True)
    address_district = models.CharField(max_length=255, blank=True, null=True)
    address_street = models.CharField(max_length=255, blank=True, null=True)
    address_corps = models.CharField(max_length=255, blank=True, null=True)
    address_apartment = models.IntegerField(blank=True, null=True)
    bremin_code = models.CharField(max_length=255, blank=True, null=True)
    counterparty_guid = models.CharField(db_column='counterparty_GUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'construction_objects'
        db_table_comment = 'MGS_╬с·хъЄ√╧ЁюхъЄшЁютрэш ╤ЄЁюшЄхы№ёЄтр'


class Counterparty(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    registration_date = models.DateField(blank=True, null=True, db_comment='─рЄр уюёєфрЁёЄтхээющ ЁхушёЄЁрЎшш')
    counterparty_head_guid = models.CharField(db_column='counterparty_head_GUID', max_length=150, blank=True, null=True, db_comment='├юыютэющ ъюэЄЁрухэЄ')  # Field name made lowercase.
    counterparty_inn = models.CharField(max_length=12, blank=True, null=True, db_comment='╙═╧')
    is_archived = models.IntegerField(blank=True, null=True, db_comment='╩юэЄЁрухэЄ т рЁїштх')
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='═ршьхэютрэшх')
    fullname = models.TextField(blank=True, null=True, db_comment='╧юыэюх эршьхэютрэшх')
    bank_account_guid = models.CharField(db_column='bank_account_GUID', max_length=150, blank=True, null=True, db_comment='╬ёэютэющ срэъютёъшщ ёўхЄ')  # Field name made lowercase.
    contract_guid = models.CharField(db_column='contract_GUID', max_length=150, blank=True, null=True, db_comment='╬ёэютэющ фюуютюЁ ъюэЄЁрухэЄр')  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', unique=True, max_length=150, blank=True, null=True, db_comment='╤ё√ыър')  # Field name made lowercase.
    counterparty_type = models.CharField(max_length=150, blank=True, null=True, db_comment='▐Ё. / Їшч. ышЎю')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'counterparties'
        db_table_comment = '╩юэЄЁрухэЄ√'


class CounterpartyOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accepted_date = models.DateTimeField(blank=True, null=True)
    departure_date = models.DateTimeField(blank=True, null=True)
    counterparty_name = models.CharField(max_length=255, blank=True, null=True)
    manager_guid = models.CharField(db_column='manager_GUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employe_name = models.CharField(max_length=255)
    temp_order_id = models.CharField(max_length=255, blank=True, null=True)
    division = models.CharField(max_length=255)
    counterparty_guid = models.CharField(db_column='counterparty_GUID', max_length=255)  # Field name made lowercase.
    construction_object_guid = models.CharField(db_column='construction_object_GUID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    order_type_id = models.IntegerField()
    bremin_code = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'counterparty_orders'
        db_table_comment = '╟р тъш эр ╬╩'


class OrderType(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    bremin_code = models.CharField(unique=True, max_length=9, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_types'
        db_table_comment = '╥шя√ чр тюъ эр ╬╩'


class WorkPackage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    work_package = models.CharField(max_length=150, blank=True, null=True, db_comment='╩юьяыхъё ЁрсюЄ')
    construct_object_guid = models.CharField(db_column='construct_object_GUID', max_length=150, blank=True, null=True, db_comment='╤ё√ыър')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'work_packages'
        db_table_comment = 'MGS_╬с·хъЄ√╧ЁюхъЄшЁютрэш ╤ЄЁюшЄхы№ёЄтр.╩юьяыхъё√╨рсюЄ'