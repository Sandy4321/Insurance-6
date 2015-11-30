from django.db import models

class Branch(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=500)
	#if name.CharField == "":
		#pass

class Underwriter(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=500)

class Customer(models.Model):
	name = models.CharField(max_length=200)
	mobileNo = models.CharField(max_length=200)
	address = models.CharField(max_length=500)

class Product(models.Model):
	sku = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	basePrice = models.CharField(max_length=200)
	sellingPrice = models.CharField(max_length=200)

class TextMessage(models.Model):
	mobileNo = models.CharField(max_length=200)
	message = models.CharField(max_length=200)