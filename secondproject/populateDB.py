import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','secondproject.settings')

import django
django.setup()

import random
from firstapp.models import AccessRecord, Website, Topic
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news','games']

def add_topic():
	t = Topic.objects.get_or_create(topic_name =  random.choice(topics))[0]
	t.save()
	return t

def populate(n = 50):

	for entry in range(n):
		# get topic for entry
		top = add_topic()

		#create fake data for website using
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		#create fake webpage
		webpg = Website.objects.get_or_create(topic=top,url_address = fake_url, title= fake_name )[0]

		#create fake accessrecord
		acc_rec = AccessRecord.objects.get_or_create(name=webpg,date = fake_date)[0]

if __name__ == '__main__':
	populate(20)
	print("Successfully Populated")
