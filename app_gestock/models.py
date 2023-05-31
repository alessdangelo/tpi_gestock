from django.db import models
from django.conf import settings

class t_borrow(models.Model):
    """
    Table representing a borrow. The relationship between a user and an article.
    """
    idBorrow = models.AutoField(primary_key=True) # Unique identifier for the borrow
    borLocation = models.CharField(max_length=50) # Location of the borrow (Home, Office, ...)
    borDate = models.DateField() # Date on which the article was borrowed
    borReturnDate = models.DateField() # Date on which the article has to be returned
    borNote = models.CharField(max_length=250) # Note for the article
    borUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Foreign key to the user table; source : https://learndjango.com/tutorials/django-best-practices-referencing-user-model
    fkArticle = models.ForeignKey('t_article', on_delete=models.CASCADE) # Foreign key to the article; source : https://learndjango.com/tutorials/django-best-practices-referencing-user-model

class t_article(models.Model):
    """
    Table representing an article, which is a product.
    """
    idArticle = models.AutoField(primary_key=True) # Unique identifier for the article
    artName = models.CharField(max_length=50) # Name of the article
    artNote = models.CharField(max_length=250) # Note for the article
    fkCupboard = models.ForeignKey('t_cupboard', on_delete=models.CASCADE) # Foreign key to the cupboard table
    fkRoom = models.ForeignKey('t_room', on_delete=models.CASCADE) # Foreign key to the room table
    fkProduct = models.ForeignKey('t_products', on_delete=models.CASCADE) # Foreign key to the product table


class t_categories(models.Model):
    """
    Table representing a category.
    """
    idCategories = models.AutoField(primary_key=True) # Unique identifier for the category
    catName = models.CharField(max_length=50) # Name of the category
    # fkType = models.ForeignKey('t_types', on_delete=models.CASCADE) # Foreign key to the type table


class t_cupboard(models.Model):
    """
    Table representing a cupboard.
    """
    idCupboard = models.AutoField(primary_key=True) # Unique identifier for the cupboard
    cupName = models.CharField(max_length=50) # Name of the cupboard
    fkRoom = models.ForeignKey('t_room', on_delete=models.CASCADE) # Foreign key to the room table


class t_products(models.Model):
    """
    Table representing a product.
    """
    idProduct = models.AutoField(primary_key=True) # Unique identifier for the product
    proName = models.CharField(max_length=75) # Name of the product
    proNote = models.CharField(max_length=250) # Note for the product
    proImage = models.CharField(max_length=500) # Image of the product
    proBoughtPrice = models.FloatField() # Price at which the product was bought
    proBoughtDate = models.DateField() # Date on which the product was bought
    fkArticle = models.ForeignKey(t_article, on_delete=models.CASCADE, null=True) # Foreign key to the article table
    fkCategory = models.ForeignKey(t_categories, on_delete=models.CASCADE) # Foreign key to the category table
    fkType = models.ForeignKey('t_types', on_delete=models.CASCADE) # Foreign key to the type table


class t_room(models.Model):
    """
    Table representing a room.
    """
    idRoom = models.AutoField(primary_key=True) # Unique identifier for the room
    rooName = models.CharField(max_length=50) # Name of the room


class t_types(models.Model):
    """
    Table representing a type.
    """
    idType = models.AutoField(primary_key=True) # Unique identifier for the type
    typName = models.CharField(max_length=50) # Name of the type
