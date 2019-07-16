from django.db import models

class TransLog(models.Model):
	person_id = models.CharField(max_length=100)
	Date = models.DateTimeField()
	pick_up_loc = models.CharField(max_length=200)
	drop_off_loc = models.CharField(max_length=200)
	Reason = models.CharField(max_length=200)
	first_time = models.IntegerField(default=0)

	def __str__(self):
		return self.person_id

class TransSurvey(models.Model):
	person_id = models.CharField(max_length=100)
	Date = models.DateTimeField()
	Question_1 = models.CharField(max_length=200)
	Question_2 = models.CharField(max_length=200)
	Question_3 = models.CharField(max_length=200)
	Question_4 = models.CharField(max_length=200)
	
	def __str__(self):
		return self.person_id
