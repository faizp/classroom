from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, unique=True, null=True)
    status = models.CharField(max_length=32, null=True)
    company = models.CharField(max_length=32, null=True)
    bio = models.TextField(max_length=None, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

