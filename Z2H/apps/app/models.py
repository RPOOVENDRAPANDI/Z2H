from django.db import models
from apps.utils.models import ZeroToHeroBaseModel

# Create your models here.

class Z2HPlanDetails(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    level_one_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_two_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_three_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_four_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)