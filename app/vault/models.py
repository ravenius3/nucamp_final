from django.db import models
import random

def pass_gen():
    return ''.join(chr(random.randint(33,126)) for num in range(random.randint(8, 20)))

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)

class Password(models.Model):
    url = models.CharField(max_length=800)
    password = models.CharField(default=pass_gen, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['url', 'user'], name='unique_url_and_user_id')
        ]