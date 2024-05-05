from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin
)
from apps.utils.models import (
    ZeroToHeroBaseModel,
    District,
)

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
        user.is_superuser = False
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Z2HUser(AbstractBaseUser, PermissionsMixin, ZeroToHeroBaseModel):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_password_updated = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Z2HCustomers(ZeroToHeroBaseModel):
    user = models.ForeignKey(Z2HUser, on_delete=models.PROTECT, related_name="users", null=False, blank=False)
    referrer = models.ForeignKey("self", on_delete=models.SET_NULL, related_name="customer", null=True, blank=True)
    active_plan_uid = models.CharField(max_length=64, null=False, blank=False)
    plan_start_date = models.DateTimeField(null=False, blank=False)
    plan_end_date = models.DateTimeField(null=True, blank=True)
    is_level_one_completed = models.BooleanField(default=False)
    is_level_two_completed = models.BooleanField(default=False)
    is_level_three_completed = models.BooleanField(default=False)
    is_level_four_completed = models.BooleanField(default=False)

class RegisterUser(ZeroToHeroBaseModel):

    MARITAL_CHOICES = (
        ('single', 'single'),
        ('married', 'married'),
    )
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    )

    referred_by = models.ForeignKey(Z2HCustomers, on_delete=models.PROTECT, related_name="users", null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='users', null=False, blank=False)
    user = models.OneToOneField(Z2HUser, on_delete=models.PROTECT, related_name="user", null=True, blank=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    nominee_name = models.CharField(max_length=128, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    marital_status = models.CharField(max_length=64, choices=MARITAL_CHOICES, null=False, blank=False)
    gender = models.CharField(max_length=64, choices=GENDER_CHOICES, null=False, blank=False)
    aadhar_number = models.CharField(max_length=12, null=False, blank=False)
    pan = models.CharField(max_length=10, null=True, blank=True)
    mobile_number = models.CharField(max_length=64, null=False, blank=False, unique=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='users', null=False, blank=False)
    city = models.CharField(max_length=128, null=False, blank=False)
    town = models.CharField(max_length=128, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    pin_code = models.CharField(max_length=6, null=False, blank=False)
    name_of_bank = models.CharField(max_length=128, null=False, blank=False)
    name_as_in_bank = models.CharField(max_length=256, null=False, blank=False)
    ifsc_code = models.CharField(max_length=11, null=False, blank=False)
    bank_branch = models.CharField(max_length=128, null=False, blank=False)
    account_number = models.CharField(max_length=64, null=False, blank=False)
    profile_photo_path = models.CharField(max_length=256, null=True, blank=True)
    email_address = models.CharField(max_length=256, null=False, blank=False)
    alternate_mobile_number = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Z2HUserRoles(ZeroToHeroBaseModel):
    user_uid = models.CharField(max_length=64, null=False, blank=False)
    role_uid = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.user_uid