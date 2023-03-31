from django.db import models

class offset(models.Model):
    #id = models.AutoField(primary_key=True)
    store_id = models.CharField(primary_key = True , max_length=30)
    loc = models.TextField()
    name = models.TextField()
    abbrevation = models.TextField()
    offset = models.DurationField()
    is_dst = models.BooleanField()
    
    
    class Meta:
        db_table = 'id_offset'
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'