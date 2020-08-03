from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, nickname, password, **kargs):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **kargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, nickname, password=None, **kargs):
        return self._create_user(email, nickname, password, **kargs)

    def create_superuser(self, email, nickname, password, **kargs):
        kargs.setdefault('is_superuser', True)
        return self._create_user(email, nickname, password, **kargs)

class User(AbstractBaseUser):
    email =  models.EmailField(unique=True)
    nickname = models.CharField(max_length=10, unique=True)
    profile_image = models.ImageField(blank=True, upload_to="profile")
    license = models.CharField(max_length=20, blank=True)
    license_image = models.ImageField(blank=True, upload_to="license")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login =  models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def get_email(self):
        return self.email
