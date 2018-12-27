from django.db import models
from .choices import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class People(models.Model):
	item_id = models.AutoField(primary_key=True)
	age = models.IntegerField(validators=[
            MaxValueValidator(150),
            MinValueValidator(1)
        ])
	workclass = models.CharField(max_length=20, choices=WORKCLASS_CHOICES)
	fnlwgt = models.IntegerField()
	education = models.CharField(max_length=15, choices=EDUCATION_CHOICES)
	education_num = models.IntegerField()
	marital_status = models.CharField(max_length=25, choices=STATUS_CHOICES)
	occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES)
	relationship = models.CharField(max_length=15, choices=RELATIONSHIP_CHOICES)
	race = models.CharField(max_length=20, choices=RACE_CHOICES)
	sex = models.CharField(max_length=7, choices=SEX_CHOICES)
	capital_gain = models.IntegerField()
	capital_loss = models.IntegerField()
	hours_per_week = models.IntegerField()
	native_country = models.CharField(max_length=30)

	def __unicode__(self):
		return self.item_id

	class meta:
		verbose_name_plural = "alldata"
		ordering = ['-item_id']

