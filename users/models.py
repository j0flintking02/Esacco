from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
                    password=None, is_staff=False, is_admin=False):
        if not email:
            return "Users must have an Email address"
        if not password:
            return 'Users must have a Password'
        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user_obj = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user_obj

    def create_superuser(self, first_name, last_name, email, password):
        user_obj = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        user_obj.save(using=self._db)
        return user_obj


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    APPROVED = 'APV'
    REJECTED = 'REJ'
    PENDING = 'PED'
    STATUS_CHOICES = [
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),
        (PENDING, 'pending'),
    ]
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_status(self):
        return self.status

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


post_save.connect(save_profile, sender=User)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=255, blank=True, null=False)
    phone = models.CharField(max_length=255, blank=True, null=False)
    occupation = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return self.user.first_name + ' \'s Profile'
