from django.contrib.auth.models import AbstractUser, Permission, Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='flags/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class DetailLanguage(models.Model):
    name = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='detaillanguage')
    subtitle = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(verbose_name='Description')
    img = models.ImageField(upload_to='detaillanguage_pic/', blank=True, null=True)
    
    def __str__(self):
        return str(self.name) + '-->' + self.subtitle


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
    img = models.ImageField(upload_to='industries/')
    text = models.TextField()

    def __str__(self):
        return self.iconText
    
    
class DetailIndustry(models.Model):
    name = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='detailindustry')
    subtitle = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(verbose_name='Description')
    img = models.ImageField(upload_to='detailindustry_pic/', blank=True, null=True)
    
    def __str__(self):
        return str(self.name) + '-->' + self.subtitle


class Review(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='reviews/logos/')
    img = models.ImageField(upload_to='reviews/images/')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    DOCUMENTS = 1
    VIDEO = 2
    AUDIO = 3
    LINK = 4

    FILE_TYPE_CHOICES = (
        (DOCUMENTS, 'Documents'),
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
        (LINK, 'Link'),
    )
    services = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    industries = models.ForeignKey(Industry, on_delete=models.SET_NULL, blank=True, null=True)
    type_file = models.IntegerField(choices=FILE_TYPE_CHOICES)
    source_language = models.ManyToManyField(Language, related_name='source_orders')
    target_language = models.ManyToManyField(Language, related_name='target_orders')
    documents = models.FileField(upload_to='order_documents/', blank=True, null=True)
    link = models.CharField(max_length=400, blank=True, null=True)
    deadline = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.services)


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    bool = models.BooleanField(default=False)

    def __str__(self):
        return self.question
    
    
class Consult(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Freelancer(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='full_name')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.IntegerField(verbose_name='Phone number')
    language1 = models.ManyToManyField(Language, related_name='language1')     
    language2 = models.ManyToManyField(Language, related_name='language2')
    
    def __str__(self):
        return self.full_name