from django.db import models
from django.contrib.auth.hashers import make_password

class MarketplaceUser(models.Model):
    USER_TYPE_CHOICES = (
        ('Customer', 'Customer'),
        ('Dealer', 'Dealer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255)
    
    # Dealer specific fields
    dealership_name = models.CharField(max_length=255, null=True, blank=True)
    dealership_type = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Hash password if it's not already hashed (simple check)
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_active(self):
        return True

    def __str__(self):
        return f"{self.full_name} ({self.phone})"
