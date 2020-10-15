from django.db import models


class UserInfo(models.Model):
    fname = models.CharField(max_length=2000)
    mname = models.CharField(max_length=2000)
    lname = models.CharField(max_length=2000)
    cname = models.CharField(max_length=2000)
    pnumber = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    dob = models.CharField(max_length=2000)
    pin = models.CharField(max_length=2000)
    district = models.CharField(max_length=2000)
    state = models.CharField(max_length=2000)
    city = models.CharField(max_length=2000)
    address = models.CharField(max_length=2000)
    aadharcard = models.FileField(null=True, blank=True)
    pancard = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.fname
