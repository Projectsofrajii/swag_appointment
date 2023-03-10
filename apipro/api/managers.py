from django.contrib.auth.base_user import BaseUserManager
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    CustomUser uses the phone as unique 
    identifier rather than username.
    """
    def create_user(self, email, name, phone, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required.'))
        if not name:
            raise ValueError(_('Name is required.'))
        if not name:
            raise ValueError(_('Phone number is required.'))
        if not password:
            raise ValueError(_('Password is required.'))

        extra_fields.setdefault('is_active', True)

        email = email
        name = name
        phone = phone
        
        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required.'))
        if not name:
            raise ValueError(_('Name is required.'))
        if not password:
            raise ValueError(_('Password is required.'))

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser mush have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser mush have is_superuser=True'))

        superuser = self.model(email=email, **extra_fields)

        superuser.name = name

        superuser.set_password(password)
        superuser.save()

        return superuser