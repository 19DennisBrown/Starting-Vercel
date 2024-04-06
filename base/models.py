from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
  profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  status = models.BooleanField(default=False)
  def __str__(self):
        return self.profile.description