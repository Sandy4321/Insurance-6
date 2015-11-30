from django.db import models

class Branch(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=500)

class Underwriter(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=500)

class Customer(models.Model):
	name = models.CharField(max_length=200)
	mobileNo = models.CharField(max_length=200)
