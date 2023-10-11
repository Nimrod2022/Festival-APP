from django.db import models
from django.contrib.gis.db import models

# Your models with PointField and PolygonField


# Create your models here.

class FoodAreas(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.PolygonField(blank=True, null=True)
    name = models.CharField(max_length=50)

    # Class definition to work with the db table as is
    class Meta:
        managed = False
        db_table = 'food_areas'

class Dustbins(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dustbins'

class FoodStalls(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    cuisine = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_stalls'

class InfoPoints(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_points'


class KidsArena(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PolygonField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kids_arena'

class Shops(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class Souvenirs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PolygonField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'souvenirs'

class Stages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PolygonField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    genre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stages'


class TrampolinePark(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trampoline_park'

class Washrooms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'washrooms'

