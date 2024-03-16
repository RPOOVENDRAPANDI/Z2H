from django.db import models
from apps.utils.models import ZeroToHeroBaseModel

# Create your models here.

class Z2HPlanDetails(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=False, blank=False)
    level_one_percentage = models.IntegerField(null=False, blank=False)
    level_two_percentage = models.IntegerField(null=False, blank=False)
    level_three_percentage = models.IntegerField(null=False, blank=False)
    level_four_percentage = models.IntegerField(null=False, blank=False)
    registration_fee = models.DecimalField(max_digits=13, decimal_places=2)