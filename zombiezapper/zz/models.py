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
#    commitments = models.ForeignKey('sites.Habit')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)



class Habit(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    trigger = models.CharField(max_length = 500)
    habit = models.CharField(max_length = 100)
#    committers = models.ManyToManyField(User, through='Commitment')
    num_commitments = models.IntegerField()
    publish_date = models.DateTimeField(
        blank = True, null = True)
    category = models.CharField(max_length = 20,
        blank = True, null = True)

    def publish(self):
        self.publish_date = timezone.now()
        num_commitments = 1
        self.save()

    def __str__(self):
        return self.trigger +" "+ self.habit

#this way I can remove num_commitments from Habit class
class Commitment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #committer
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE) #commitment
    date_commited = models.DateField(
        blank = True, null = True)
    def __str__(self):
        return self.habit.trigger +" - "+str(self.habit.author)
    def publish(self):
        self.date_commited = timezone.now()
        self.save()
#    @receiver(post_save, sender=User)
