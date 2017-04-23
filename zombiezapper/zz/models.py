from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class User(models.Model):
	user = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	statement = models.CharField(max_length = 150)
	level = models.IntegerField()
#	commitments = models.ForeignKey('sites.Habit')

	def __str__(self):
		return user

class Habit(models.Model):
	author = models.ForeignKey('auth.User')
	trigger = models.CharField(max_length = 500)
	habit = models.CharField(max_length = 100)
	num_commitments = models.IntegerField()
	publish_date = models.DateTimeField(
		blank = True, null = True)
#	comments = 

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.trigger + self.habit