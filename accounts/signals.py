from .models import User, UserProfile
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print('created')
    if created:
        UserProfile.objects.create(user=instance)
        print('create the user profile')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('user is updated.')
        except:
            #create the user profile if not existed..
            UserProfile.objects.create(user=instance)
            
            print('user profile is created.')


# post_save.connect(post_save_create_profile_receiver, sender=User)  

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'This user is being saved.')