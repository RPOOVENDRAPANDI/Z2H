from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin
)

from apps.utils.models import ZeroToHeroBaseModel

# Create your models here.

class Role(ZeroToHeroBaseModel):
    LOGIN_MODE_CHOICES = (
        ('web', 'web'),
        ('mobile', 'mobile'),
    )

    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    login_mode = models.CharField(max_length=64, choices=LOGIN_MODE_CHOICES, default='mobile')

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_field):
        """Create, save and returns a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.is_active = False
        user.is_superuser = False
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

class Z2HUser(AbstractBaseUser, PermissionsMixin, ZeroToHeroBaseModel):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    

class Z2HUserDetails(ZeroToHeroBaseModel):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    )

    user = models.ForeignKey(Z2HUser, on_delete=models.CASCADE, related_name='users', null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='users', null=False, blank=False)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=64, choices=GENDER_CHOICES, default='male', null=False, blank=False)
    mobile_number = models.CharField(max_length=15, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    aadhar_number = models.CharField(max_length=12, null=False, blank=False)
    aadhar_image = models.CharField(max_length=256, null=False, blank=False)
    pan_number = models.CharField(max_length=10, null=False, blank=False)
    pan_image = models.CharField(max_length=256, null=False, blank=False)
    bank_account_number = models.CharField(max_length=64, null=False, blank=False)
    bank_account_name = models.CharField(max_length=128, null=False, blank=False)
    ifsc_code = models.CharField(max_length=11, null=False, blank=False)
    user_image = models.CharField(max_length=256, null=False, blank=False)


