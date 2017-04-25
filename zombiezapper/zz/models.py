from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	statement = models.CharField(max_length = 250, blank=True)
	level = models.IntegerField(default=1)
#	commitments = models.ForeignKey('sites.Habit')

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
	
	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, created, **kwargs):
		instance.profile.save()

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