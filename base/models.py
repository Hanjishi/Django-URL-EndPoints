from django.db import models

class SampleTb(models.Model):
    attribute_1 = models.CharField(max_length=100)
    attribute_2 = models.TextField()

    class Meta:
        db_table = 'sample_tb'

    def __str__(self):
        return self.attribute_1

class TextRecord(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]