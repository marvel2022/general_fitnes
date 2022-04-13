from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Kategoriya Nomi')
    slug = models.SlugField(max_length=300, verbose_name='Slug')

    image = models.ImageField(upload_to='category-image/', blank=True, null=True, verbose_name='Rasm')
    caption = models.CharField(max_length=300, blank=True, null=True, verbose_name='Rasm Sarlavhasi')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    class Meta:
        verbose_name    = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', verbose_name='Kategoriya')

    name = models.CharField(max_length=200, verbose_name='Nomi')
    product_model = models.CharField(max_length=100, unique=True, verbose_name='Maxsulot Modeli')
    slug = models.SlugField(max_length=300, verbose_name='Slug')
    description = models.TextField(verbose_name='Tarifi')

    guarentee = models.CharField(max_length=200, blank=True, null=True, verbose_name="Kafolat: ")

    delivery_uzb = models.BooleanField(default=False, verbose_name='O\'zbekiston bo\'ylab yetkazib berish')
    delivery_toshkent = models.BooleanField(default=False, verbose_name='Toshkent bo\'ylab yetkazib berish')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Maxsulot"
        verbose_name_plural="Maxsulotlar"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image", verbose_name='Maxsulot')

    image = models.ImageField(upload_to="product-image/", verbose_name='Rasmlar')
    caption = models.CharField(max_length=300, blank=True, null=True, verbose_name='Rasm Sarlavhasi')

    def __str__(self):
        return str(self.pk)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url