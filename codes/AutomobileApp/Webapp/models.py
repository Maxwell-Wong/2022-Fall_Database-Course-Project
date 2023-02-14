# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    brand_id = models.CharField(primary_key=True, max_length=8)
    brand_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'brand'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=8)
    customer_name = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    annual_income = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Dealer(models.Model):
    dealer_id = models.CharField(primary_key=True, max_length=8)
    dealer_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dealer'


class ManufacturingPlant(models.Model):
    plant_id = models.CharField(primary_key=True, max_length=8)
    plant_name = models.CharField(max_length=20)
    part_name = models.CharField(max_length=20, blank=True, null=True)
    assembler = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'manufacturing_plant'


class Model(models.Model):
    model_id = models.CharField(primary_key=True, max_length=8)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    model_name = models.CharField(max_length=20)
    body_style = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class Options(models.Model):
    option_id = models.CharField(primary_key=True, max_length=8)
    color = models.CharField(max_length=20, blank=True, null=True)
    engine = models.CharField(max_length=20, blank=True, null=True)
    transmission = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class Sold(models.Model):
    vin = models.OneToOneField('Vehicle', models.DO_NOTHING, db_column='VIN', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    sale_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sold'
        unique_together = (('vin', 'customer'),)


class Supplier(models.Model):
    supplier_id = models.CharField(primary_key=True, max_length=8)
    supplier_name = models.CharField(max_length=20)
    part_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class Supply(models.Model):
    supplier = models.OneToOneField(Supplier, models.DO_NOTHING, primary_key=True)
    model = models.ForeignKey(Model, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supply'
        unique_together = (('supplier', 'model'),)


class Vehicle(models.Model):
    vin = models.CharField(db_column='VIN', primary_key=True, max_length=20)  # Field name made lowercase.
    model = models.ForeignKey(Model, models.DO_NOTHING, blank=True, null=True)
    option = models.ForeignKey(Options, models.DO_NOTHING, blank=True, null=True)
    plant = models.ForeignKey(ManufacturingPlant, models.DO_NOTHING, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle'
