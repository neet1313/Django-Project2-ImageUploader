from django.db import models

# Since we're working with Images here so install pillow
# -> pip install pillow


class Image(models.Model):
    photo = models.ImageField(upload_to='myImages')
    date = models.DateTimeField(auto_now_add=True)
