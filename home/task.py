import csv
import os
from .models import People

def save_data():
	with open('home/data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			# print(row.keys())
			p = People(age=row['Age'], workclass=row['Workclass'][1:], fnlwgt=row['Fnlwgt'][1:],
				education=row['Education'][1:], education_num=row['Education_num'][1:],
				marital_status=row['Marital_status'][1:], occupation=row['Occupation'][1:],
				relationship=row['Relationship'][1:], race=row['Race'][1:], sex=row['Sex'][1:],
				capital_gain=row['Capital_gain'][1:], capital_loss=row['Capital_loss'][1:],
				hours_per_week=row['Hours_per_week'][1:], native_country=row['Native_country'][1:])
			p.save()