from django.db import models

# Create your models here.
class DataStore(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.TextField()
    Phone = models.CharField(max_length=100)
    Location = models.CharField(max_length=120,blank="True", null="True")
    Type = models.TextField()
    Status = models.TextField()

    def __str__(self):
        return f"{self.Name} | {self.Location} | {self.Phone} | {self.Type} | {self.Status}"

