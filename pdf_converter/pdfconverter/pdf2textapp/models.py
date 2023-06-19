from django.db import models

class Text(models.Model):
    text = models.TextField()
    file_associated = models.ForeignKey('File', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class File(models.Model):
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.document.name
