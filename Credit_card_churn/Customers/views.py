from django.shortcuts import render
from .models import Customer
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from rest_framework.views import APIView
import csv, io
from django.core.paginator import Paginator


class ViewCustomerData(APIView):
	def get(self, request):
		params = request.GET.dict()
		param = {}
		for key, value in params.items():
			if params[key] and key != 'page':
				param[key] = value
		customers = Customer.objects.filter(**param)
		paginator = Paginator(customers, 5)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(
						request, 
						'customer_filter.html', 
						{'page_obj': page_obj}
					)
		

def is_float(n):
	try:
		float_n = float(n)
		return float_n
	except ValueError:
		return None


def SaveCustomerData(request):
	data={}
	
	if "GET" == request.method:
		return render(request, "customer_upload.html", data)
	try:
		csv_file = request.FILES["csv_file"]
		
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("save_customer"))

		data_set = csv_file.read().decode('UTF-8')
		io_string = io.StringIO(data_set)
		customers = []
		next(io_string)
		for column in csv.reader(io_string, delimiter=',', quotechar="|"):
			customers.append(
				Customer(
					client_num=column[0],
					attrition_flag=column[1],
					age=column[2],
					gender=column[3],
					dependent_count=column[4],
					education_level=column[5],
					marital_status=column[6],
					income_category=column[7],
					card_category=column[8],
					months_on_book=column[9],
					relation_count=column[10],
					months_inactive=column[11],
					contacts_count=column[12],
					credit_limit=column[13],
					revolving_bal=column[14],
					avg_open_to_buy=column[15],
					amt_chg=column[16],
					trans_amt=column[17],
					trans_ct=column[18],
					ct_change=column[19],
					avg_utilization_ratio=column[20],
					naive_bayes_1=is_float(column[21]),
					naive_bayes_2=is_float(column[22]),
					)
				)
		Customer.objects.bulk_create(customers)
	except Exception as e:
		messages.error(request,"Unable to upload file. "+repr(e))

	context = {}
	return HttpResponseRedirect(reverse("save_customer"))



