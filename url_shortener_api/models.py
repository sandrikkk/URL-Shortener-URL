from django.db import models
from string import ascii_letters
from random import choices
from django.conf import settings
# Create your models here.


class Link(models.Model):
    original_link = models.URLField(max_length=250)
    shortened_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    custom_url = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        ordering = ('-created_at',)
    
    def increase_short_id_counter(self):
        self.count += 1
        self.save()

    # def shortener(self):
    #     while True:
    #         random_string = ''.join(choices(ascii_letters, k=6))
    #         link = settings.HOST_URL + '/' + random_string
    #         if not Link.objects.filter(shortened_link = link).exists():
    #             break
    #     return link
    #
    # def save(self, *args, **kwargs):
    #     if not self.shortened_link:
    #         link = self.shortener()
    #         self.shortened_link = link
    #     return super().save(*args, **kwargs)
