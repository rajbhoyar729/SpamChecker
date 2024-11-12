from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, phone, name, password=None, email=None):
        if not phone:
            raise ValueError("Users must have a phone number")
        user = self.model(phone=phone, name=name, email=email)
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name, password):
        user = self.create_user(phone=phone, name=name, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    groups = models.ManyToManyField( 'auth.Group', related_name='custom_user_set' # Change this to a unique name 
                                    )
    user_permissions = models.ManyToManyField( 'auth.Permission', related_name='custom_user_permissions_set' # Change this to a unique name 
                                              )
    
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

# Contact model
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.phone})"

# Spam report model
class SpamReport(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="spam_reports")
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Spam Report - {self.phone_number} by {self.reported_by}"

