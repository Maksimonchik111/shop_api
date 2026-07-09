import random
from django.db import models
from django.contrib.auth.models import User

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.user}-{self.token}'

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        super().save(*args, **kwargs)