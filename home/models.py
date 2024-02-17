from django.db                  import models
from django.utils.translation   import gettext_lazy as _
from django.utils.text          import slugify
from django.urls                import reverse
from datetime                   import datetime
from django.contrib.auth.models import User
# Create your models here.

RATING = (
    (1,'★☆☆☆☆'),
    (2,'★★☆☆☆'),
    (3,'★★★☆☆'),
    (4,'★★★★☆'),
    (5,'★★★★★'),
)


class product(models.Model):
    title       = models.CharField     (max_length=20, verbose_name=_('name'))
    description = models.TextField     (blank=True, null=True)
    price       = models.DecimalField  (max_digits=9, decimal_places=3, verbose_name=_('price'))
    category    = models.ForeignKey    ('category', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('category'))
    img         = models.ImageField    (upload_to='product/years=%y/month=%m', default='default.png', verbose_name=_('image'))
    slug        = models.SlugField     (blank=True,null=True, verbose_name=_('slug'))
    active      = models.BooleanField  (default = True, verbose_name=_('active'))
    date        = models.DateTimeField (default=datetime.now())
    
    date1       = models.DateTimeField (auto_now=True)
    date2       = models.DateTimeField (auto_now_add=True)
    
    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("products")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    
    
class category(models.Model):
    catname = models.CharField (max_length=50, verbose_name=_('name'))
    catslug = models.SlugField (max_length=200, verbose_name=_('slug'), blank=True, null=True)
    
    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Categories")
    
    def save(self, *args, **kwargs):
        if not self.catslug:
            self.catslug = slugify(self.catname)
        super(category, self).save(*args, **kwargs)
    

    
    def __str__(self):
        return self.catname


### review ### 
class ProductReview(models.Model):
    user    = models.ForeignKey    (User,    on_delete=models.SET_NULL, null=True) 
    product = models.ForeignKey    (product, on_delete=models.SET_NULL, null=True)
    review  = models.TextField     (blank=True, null=True)
    rating  = models.IntegerField  (choices=RATING, default=None)
    date    = models.DateTimeField (auto_now_add=True)
    
    class Meta:
        verbose_name        = _("Review")
        verbose_name_plural = _("Reviews")
        
    def __str__(self):
        return str(self.product.title)
    
    def get_rating(self):
        return self.rating