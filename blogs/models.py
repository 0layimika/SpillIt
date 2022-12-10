from django.db import models
from django.contrib.auth.models import User
class blog(models.Model):
    title = models.CharField(max_length=230)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    like = models.IntegerField(default=1)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
# Create your models here.
