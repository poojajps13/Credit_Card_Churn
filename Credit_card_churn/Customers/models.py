from django.db import models

class Customer(models.Model):
	client_num = models.IntegerField(unique=True)
	attrition_flag = models.CharField(max_length=50, null=True)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=1, null=True)
	dependent_count = models.IntegerField(null=True)
	education_level = models.CharField(max_length=50, null=True)
	marital_status = models.CharField(max_length=10, null=True)
	income_category = models.CharField(max_length=50, null=True)
	card_category = models.CharField(max_length=10, null=True)
	months_on_book = models.IntegerField(null=True)
	relation_count = models.IntegerField(null=True)
	months_inactive = models.IntegerField(null=True)
	contacts_count = models.IntegerField(null=True)
	credit_limit = models.FloatField(null=True)
	revolving_bal = models.FloatField(null=True)
	avg_open_to_buy = models.FloatField(null=True)
	amt_chg = models.FloatField(null=True)
	trans_amt = models.FloatField(null=True)
	trans_ct = models.FloatField(null=True)
	ct_change = models.FloatField(null=True)
	avg_utilization_ratio = models.FloatField(null=True)
	naive_bayes_1 = models.FloatField(null=True)
	naive_bayes_2 = models.FloatField(null=True)

	def __str__(self):
		return str(self.client_num)