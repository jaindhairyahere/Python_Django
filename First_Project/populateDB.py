import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',	'First_Project.settings')

import django
django.setup()

# Fake Population Script

import random
from firstapp.models import Company,Person
from faker import Faker

faker = Faker()

firstNames = ['Dhairya','Anubhav','Ishita','Riya','Kanishk','Muski']
def add_person():
	fake_date = faker.date()
	fake_mail = faker.company_email()
	t = Person.objects.get_or_create(name = random.choice(firstNames),dob = fake_date, email = fake_mail)[0]

	t.save()
	return t

def populate(N=100):
	for entry in range(N):
		person = add_person()

		fake_company = faker.company()
		company = Company.objects.get_or_create(com_id = person, name = fake_company)[0]

if __name__ == '__main__':
	print("Hey! Running Populating Script")
	populate(50)
	print("Successfully Populated")
