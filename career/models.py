from django.db import models

from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

