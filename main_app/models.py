from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
# many to many model
class Playdate(models.Model):
   date = models.DateField()
   time = models.TimeField()
   location = models.CharField(max_length=250)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
       return reverse ('playdates_detail', kwargs={'pk': self.pk})

#main model
class Baby(models.Model):
   name = models.CharField(max_length=100)
   date_of_birth = models.DateField('Date of Birth')
   height = models.FloatField('Height (cm)')
   weight = models.FloatField('Weight (lb)')
   playdate = models.ManyToManyField(Playdate)
   user = models.ForeignKey(User, on_delete=User)

   def get_absolute_url(self):
      return reverse('detail', kwargs={'baby_id': self.pk})

class Photo(models.Model):
   url = models.CharField(max_length=200)
   baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

   def __str__(self):
      return f'Photo for baby_id: {self.baby_id} @{self.url}'

#I updated this from breakfast, lunch, and dinner to morning, afternoon, and evening.
MEALS = (
   ('M', "Morning"),
   ('A', "Afternoon"),
   ('E', "Evening"),
)

#one to many
class Feeding(models.Model):
   date = models.DateField('Feeding Date')
   time = models.TimeField()
   meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
   )
   amount = models.FloatField("Amount (ml)")
   baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"

   class Meta:
      ordering = ['-date']


DIAPERTYPE = (
   ('1', "Pee"),
   ('2', "Poo"),
)

class Diaper(models.Model):
   date = models.DateField('Change Date')
   time = models.TimeField('Change Time')
   type = models.CharField(
      max_length=1,
      choices=DIAPERTYPE,
      default = DIAPERTYPE[0][0]
   )
   baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
   
   def __str__(self):
      return f"{self.get_diaper_display()} on {self.date}"
   
   class Meta:
      ordering = ['-date']

SLEEPTYPE = (
   ('n', 'Nap'),
   ('s', 'Sleep'),
)

class Sleep(models.Model):
   date = models.DateField('Sleep Date')
   startTime = models.TimeField('Start Time')
   endTime = models.TimeField('End Time')
   type = models.CharField(
      max_length=1,
      choices=SLEEPTYPE,
      default=SLEEPTYPE[0][0],
   )
