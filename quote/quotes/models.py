from django.db import models

from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        db_table = 'author'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('quote:author-quote-list', args=[self.name])    



class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True) 

    class Meta:
        db_table = 'tag'

    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse('quote:tag-quote-list', args=[self.name])



class Quote(models.Model):
    text = models.TextField(unique=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author,on_delete=models.PROTECT,related_name='quotes',to_field='name')

    class Meta:
        db_table = 'quote'

    def __str__(self) -> str:
        return self.text   

