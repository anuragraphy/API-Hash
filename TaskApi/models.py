from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
#base model which cannot be initialised
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True

#The Task Model class which contains all the required data for the tasks
class TaskModel(BaseModel):
    taskName = models.CharField(max_length=100)
    impact = models.IntegerField()
    ease = models.IntegerField()
    confidence = models.IntegerField()
    average = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True, blank=True)