from django.db import models

class Customer(models.Model):
	client_num = models.IntegerField(unique=True)
	attrition_flag = models.CharField(max_length=50)
	age = models.IntegerField()
	gender = models.CharField(max_length=1)
	dependent_count = models.IntegerField()
	education_level = models.CharField(max_length=50)
	marital_status = models.CharField(max_length=10)
	income_category = models.CharField(max_length=50)
	card_category = models.CharField(max_length=10)
	months_on_book = models.IntegerField()
	relation_count = models.IntegerField()
	months_inactive = models.IntegerField()
	contacts_count = models.IntegerField()
	credit_limit = models.FloatField()
	revolving_bal = models.FloatField()
	avg_open_to_buy = models.FloatField()
	amt_chg = models.FloatField()
	trans_amt = models.FloatField()
	trans_ct = models.FloatField()
	ct_change = models.FloatField()
	avg_utilization_ratio = models.FloatField()
	naive_bayes_1 = models.FloatField(null=True)
	naive_bayes_2 = models.FloatField(null=True)

	def __str__(self):
		return str(self.client_num)