from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='services/', blank=False)

    def __str__(self):
        return self.title


class Client(models.Model):
    icon = models.ImageField(upload_to='clients/', blank=False)
