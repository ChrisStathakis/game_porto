from django.db import models
import datetime
# Create your models here.

class Contact(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    first_name = models.CharField(max_length=70,)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(blank=True, null=True, max_length=10)
    message = models.TextField()
    is_readed = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name