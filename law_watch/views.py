#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from law_watch import models

'''def watch(request):
	template = loader.get_template('law_watch/index.html')
	return HttpResponse(template.render(request))'''
	
def watch(request):
	law_lists = models.BillInfoList.objects.all()
	return render(request, 'law_watch/index.html', {'lawlist' : law_lists})

def detail(request, billId):
	billRow = models.BillInfoList.objects.filter(bill_id=billId)
	return render(request, 'law_watch/detail.html', {'billId' : billRow[0]})
