from django.db import models
from apps.users.models import User


class Resume(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    # property damage risk
    expected_tenancy_length = models.IntegerField(default=1)
    total_household_members = models.IntegerField(default=1)
    consent_criminal_check = models.BooleanField(default=True)
    consent_credit_check = models.BooleanField(default=True)
    eviction_history = models.BooleanField()
    current_property_has_infestations = models.BooleanField()
    has_pet = models.BooleanField()

    # financial risk
    currently_working = models.BooleanField()
    current_ocupation = models.CharField(max_length=255, null=True)
    maximum_rental_budget = models.FloatField()
    total_household_income = models.FloatField(default=0)
    current_wage = models.FloatField(null=True)

    def __str__(self):  # title on dashboard
        return self.tenant.username

