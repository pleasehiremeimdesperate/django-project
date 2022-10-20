from django.db.models.signals import post_save, pre_save
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile created") #test shavad

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwarg):
    instance.profile.save()
    print("prof saved")