from django.db import models

# Create your models here.


class HomePicture(models.Model):
    image   = models.ImageField(upload_to='home-image/', blank=True, null=True, verbose_name="Assosiy rasm")
    caption = models.CharField(max_length=400, blank=True, null=True, verbose_name="Rasm teksti")

    active = models.BooleanField(default=False, verbose_name='Aktiv Rasm')

    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name="Assosiy Rasm"
        verbose_name_plural="Assosiy Rasmlar"
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url


class About(models.Model):
    image      = models.ImageField(upload_to="about-image/", blank=True, null=True, verbose_name="Rasm")
    caption    = models.CharField(max_length=300, blank=True, null=True, verbose_name="Rasm teksti")
    about_text = models.TextField(verbose_name="Malumot")

    active = models.BooleanField(default=False, verbose_name='Aktiv')

    def __str__(self):
        return str(self.pk)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
    class Meta:
        verbose_name="Kampaniya Haqida"
        verbose_name_plural="Kampaniya Haqida"

class FeedBack(models.Model):
    name        = models.CharField(max_length=255, blank=True, null=True, verbose_name='Mijoz Ismi')
    phonenumber = models.CharField(max_length=14, blank=True, null=True, verbose_name='Telefon Raqami')
    message     = models.TextField(blank=True, null=True, verbose_name='Habar')

    def __str__(self):
        return f"{self.name} | {self.phonenumber}"
    class Meta:
        verbose_name="Xabar"
        verbose_name_plural="Xabarlar"
