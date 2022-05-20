from django.db import models
# we want to connect it with the built-in User Model
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=500)

    def __str__(self):
        return str(self.author) + ' | ' + str(self.id)
