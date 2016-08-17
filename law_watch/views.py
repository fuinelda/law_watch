#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.views import generic

from law_watch import models

class WatchView(generic.ListView):
	template_name = 'law_watch/index.html'
	context_object_name = 'lawlist'
	
	def get_queryset(self):
		return {'all' : models.BillInfoList.objects.all()[:3], \
		'saenuri' :  models.BillInfoList.objects.filter(bill_member_json__item__contains = '[{"polyNm":"새누리당"}]'),
		'kukmin' :  models.BillInfoList.objects.filter(bill_member_json__item__contains = '[{"polyNm":"국민의당"}]'),
		'together' :  models.BillInfoList.objects.filter(bill_member_json__item__contains = '[{"polyNm":"더불어민주당"}]')}
	
	def get_by_party():
		return "파티다!"

class DetailView(generic.DetailView):
	model = models.BillInfoList
	template_name = 'law_watch/detail.html'
