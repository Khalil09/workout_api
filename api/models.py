from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Exercise(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey('auth.User', related_name='workouts', on_delete=models.CASCADE)
    exercise = models.ManyToManyField(Exercise, through='Set')

    def __str__(self):
        return self.name
    
class Set(models.Model):
    sets = models.PositiveIntegerField(default=1)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.sets