from django.db import models
from django.core.validators import MinLengthValidator , MaxLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email_address= models.EmailField(max_length=254)
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.caption}"


class Post(models.Model):
    title=models.CharField(max_length=50)
    excerpt=models.CharField( max_length=50)
    date= models.DateField( auto_now=True)
    slug= models.SlugField(unique = True, db_index= True)
    content = models.TextField(validators =[MinLengthValidator(10)])
    image_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name ="posts")
    tags = models.ManyToManyField(Tag)


