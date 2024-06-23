import uuid

from django.db import models

class ZeroToHeroBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        abstract = True

class State(ZeroToHeroBaseModel):
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.name

class District(ZeroToHeroBaseModel):
    state = models.ForeignKey(State, on_delete=models.PROTECT, null=False, blank=False)
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name

class Z2HSettings(ZeroToHeroBaseModel):
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(blank=True)
    value = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.name