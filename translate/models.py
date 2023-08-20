from django.core.exceptions import ValidationError
from django.db import models


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class LatestUpdate(models.Model):
    title = models.CharField(max_length=100)
    iconText = models.CharField(max_length=50)
    img = models.ImageField(upload_to='latest_update/')
    text = models.TextField()
    hashtag = models.ManyToManyField(Hashtag)
    icon = models.CharField(max_length=50)

    def validate_title_length(self, value):
        if len(value) < 5:
            raise ValidationError("Title must be at least 5 characters long.")

    def clean(self):
        self.validate_title_length(self.title)

    def __str__(self):
        return self.title


class OurOffer(models.Model):
    miniText = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='our_offers/', blank=True, null=True)
    bool = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title


class Industry(models.Model):
    iconText = models.CharField(max_length=50)
    Img = models.ImageField(upload_to='industries/')
    text = models.TextField()

    def __str__(self):
        return self.iconText


class Review(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='reviews/logos/')
    img = models.ImageField(upload_to='reviews/images/')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    bool = models.BooleanField(default=False)

    def __str__(self):
        return self.question