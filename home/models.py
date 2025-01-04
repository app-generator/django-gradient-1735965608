# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employee_Info(models.Model):

    #__Employee_Info_FIELDS__
    employee_id = models.TextField(max_length=255, null=True, blank=True)
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)
    group = models.TextField(max_length=255, null=True, blank=True)
    pbx = models.TextField(max_length=255, null=True, blank=True)
    residence_phone = models.TextField(max_length=255, null=True, blank=True)
    mobile = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)

    #__Employee_Info_FIELDS__END

    class Meta:
        verbose_name        = _("Employee_Info")
        verbose_name_plural = _("Employee_Info")


class Holidays(models.Model):

    #__Holidays_FIELDS__
    holiday_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    day = models.TextField(max_length=255, null=True, blank=True)
    occassion = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)

    #__Holidays_FIELDS__END

    class Meta:
        verbose_name        = _("Holidays")
        verbose_name_plural = _("Holidays")


class Punch_Records(models.Model):

    #__Punch_Records_FIELDS__
    employee_id = models.TextField(max_length=255, null=True, blank=True)
    punch_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    punch_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    device_id = models.TextField(max_length=255, null=True, blank=True)

    #__Punch_Records_FIELDS__END

    class Meta:
        verbose_name        = _("Punch_Records")
        verbose_name_plural = _("Punch_Records")


class Device_Info(models.Model):

    #__Device_Info_FIELDS__
    device_location = models.TextField(max_length=255, null=True, blank=True)
    details = models.TextField(max_length=255, null=True, blank=True)

    #__Device_Info_FIELDS__END

    class Meta:
        verbose_name        = _("Device_Info")
        verbose_name_plural = _("Device_Info")



#__MODELS__END
