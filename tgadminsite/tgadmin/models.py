from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Categories(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name


class Clients(models.Model):
    id = models.UUIDField(primary_key=True)
    tg_id = models.CharField()

    class Meta:
        managed = False
        db_table = 'clients'

    def __str__(self):
        return self.tg_id


class Orders(models.Model):
    id = models.UUIDField(primary_key=True)
    cart = models.TextField()  # This field type is a guess.
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    delivery_address = models.CharField()

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return str(self.id)


class Products(models.Model):
    id = models.UUIDField(primary_key=True)
    image_path = models.CharField()
    description = models.CharField()
    price = models.IntegerField()
    subcategory = models.ForeignKey('Subcategories', models.DO_NOTHING, db_column='subcategory', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self):
        return str(self.id)


class Subcategories(models.Model):
    name = models.CharField(primary_key=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategories'

    def __str__(self):
        return self.name
