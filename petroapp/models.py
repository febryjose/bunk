from django.db import models
from django.contrib.auth.models import User

class PetroBunk(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "PetroBunk"
	verbose_name_plural = "PetroBunks"

    def __unicode__(self):
        return self.name

class Machine(models.Model):
    """
    Model for machines.
    """
    CHOICES = (
        ('red', 'RED'),
        ('green', 'GREEN'),    
    )
    name = models.CharField(max_length=50)
    fuel = models.CharField(max_length=5, choices=CHOICES)
    class Meta:
        verbose_name = "Machine"
	verbose_name_plural = "Machines"

    def __unicode__(self):
        return self.name

class DailyInputs(models.Model):
    """
    Models for storing daily activities of user.
    """
    CHOICES = (
        ('red', 'RED'),
        ('green', 'GREEN'),    
	)
    user = models.ForeignKey(User, related_name='user_set')
    machine = models.ForeignKey(Machine, related_name="machines")
    start_reading = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    end_reading = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=5, choices=CHOICES)

    class Meta:
        verbose_name = "Daily Detail"
        verbose_name_plural = "Daily Details"

    def __unicode__(self):
        return str(self.user)

class FuelAvailability(models.Model):
    """
    Models for storing fuel levels in each machine.
    """
    CHOICES = (
        ('red', 'RED'),
        ('green', 'GREEN'),    
	)
    machine_fuel = models.ForeignKey(Machine, related_name="machine_fuel")
    litre = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    fu_type = models.CharField(max_length=5, choices=CHOICES)

    class Meta:
        verbose_name = "Fuel Availability"
        verbose_name_plural = "Fuel Availabilities"

    def __unicode__(self):
        return str(self.litre)

class AttendanceRecord(models.Model):
    user = models.ForeignKey(User)
    status = models.BooleanField(default=False)
    date = models.DateField(null=True,blank=True)
    checkin_time = models.DateTimeField(null=True,blank=True)
    checkout_time = models.DateTimeField(null=True,blank=True)
    machine = models.ForeignKey(Machine,null=True)
    start_reading = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    end_reading = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    collection = models.DecimalField(max_digits=9, decimal_places=2,null=True,blank=True)
    def __unicode__(self):
        return str(self.user)
