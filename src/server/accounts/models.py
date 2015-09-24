from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    user = models.OneToOneField(User)
    # role = models.CharField(max_length=42)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True, null=True)
    newsletter = models.BooleanField(default=False)


    def __str__(self):
        return "{0}'s profil".format(self.user.username)
