from django.db import models
from shared.models import TimeStampMixin
from django.contrib.auth.models import User

class Category(TimeStampMixin):
    category_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.category_name
    

class Post(TimeStampMixin):
    STATUS_CHOICES=[
        ('draft','DRAFT'),
        ('publised','PUBLISHED')
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    category_name = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='draft')
    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.category_name}-{self.title}"



class Comment(TimeStampMixin):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )
    body = models.TextField()
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )