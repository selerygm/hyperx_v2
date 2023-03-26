from django.db import models
from PIL import Image
from django.urls import reverse


class Product(models.Model):
    HEADPHONES = 'headphones'
    MOUSE = 'mouse'
    MICROPHONES = 'microphones'
    KEYBOARDS = 'keyboards'
    MONITORS = 'monitors'

    CHOICE_GROUP = {
        (HEADPHONES, 'headphones'),
        (MOUSE, 'mouse'),
        (MICROPHONES, 'microphones'),
        (KEYBOARDS, 'keyboards'),
        (MONITORS, 'monitors'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    discsecond = models.TextField(blank=True)
    discthirs = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=HEADPHONES)
    img = models.ImageField(default='no_image.webp', upload_to='product_image')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('products', kwargs={"product_id": self.pk})
