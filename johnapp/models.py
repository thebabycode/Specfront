from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Register(models.Model):
    event_name = models.CharField(max_length=100)
    event_type_choices = [('Web3', 'Web3'), ('Blockchain', 'Blockchain'), ('IoT', 'IoT'), ('Data Analytics', 'Data Analytics'), ('Ethereum', 'Ethereum')]
    event_type = models.CharField(max_length=100, choices=event_type_choices)
    event_date = models.DateField()
    duration = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    target_group_choices = [('Students', 'Students'), ('Employees', 'Employees'), ('Both', 'Both')]
    target_group = models.CharField(max_length=100, choices=target_group_choices)

    def __str__(self):
        return self.event_name

class pool(models.Model):

    name = models.CharField(_("name"),max_length=100)
    fname = models.CharField(_("fname"),max_length=100,null=False,blank=True)
    lname = models.CharField(_("lname"),max_length=100,null=False,blank=True)
    email = models.CharField(_("email"),max_length=100)
    occupation = models.CharField(_("occupation"),max_length=100)
    location = models.CharField(_("location"),max_length=100)
    pnumber = models.CharField(_("pnumber"),max_length=100)
    interest = models.CharField(_("interest"),max_length=100)