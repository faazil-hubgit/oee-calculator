

from .serializers import machine0,oee_information
from .serializers import product_log0
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from.models import machines
from.models import product_log
from datetime import datetime
from django.shortcuts import render,redirect



# Create your views here.



#machine details display

class mdisplay(APIView):
    def get(self,request):
        machines0=machines.objects.all()
        s=machine0(machines0,many=True)
        return Response(s.data)

#product_log details display
#product_log=modeltable
#product_log0=serializerclass



class product_display(APIView):
    def get(self,request):
        product_logs0 = product_log.objects.all()
        s1 = product_log0(product_logs0, many=True)
        return Response(s1.data)

#indexpage
class oee_info(APIView):
    def get(self,request):
        oee_information0=oee.objects.all()
        s3 =oee_information(oee_information0, many=True)
        return Response(s3.data)

def index(request):
    return render(request,'index1.html')
#OEE CALCULATION
#product produce calaculation





#ideal cycletime calculation=total duration / toatal product(time taken to produce one part)



#unplanneddowntime=shift hours-total hours
#consider shift hour= 1 hour
import calendar
import time


def machine_update(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']



        machines.objects.create(machine_name=a,machine_serial_no=b,time=c)
        return render(request, 'index1.html',)

#counting of good products

def machine_get(request):
    a=machines.objects.all()
    return render(request,'product.html',{'b':a})




def product_udt(request):

    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        e = request.POST['n5']
        c_convert_time=datetime.strptime(c,'%H:%M:%S')
        struct_time = c_convert_time.utctimetuple()
        c_convert_float = abs(calendar.timegm(struct_time))
        d_convert_time = datetime.strptime(d,'%H:%M:%S')
        struct_time=d_convert_time.utctimetuple()

        d_convert_float=abs(calendar.timegm(struct_time))
        durations=abs(d_convert_float - c_convert_float)/60

        good_product_count=int(durations / 5)
        bad_product_='1'
        product_log.objects.create(cycle_no=a,material_name=b,start_time=c,end_time=d,duration=durations,machine=e,
        good_products=good_product_count,bad_product=bad_product_)

        return redirect(machine_get)


def machine_s(request):
    a = machines.objects.all()
    return render(request, 'Oee.html', {'b': a})

from django.db.models import Sum

#OVERALL EQUIPMENT EFFECTIVENESS
#OEE=AVAILABLITY * PERFORMENCE * QUALITY
from.models import oee
def OEE_CALCULATION(request):
    if request .method=='POST':
        request.a=request.POST['n1']


  #availiblty=availabe time - unplanned downtime * 100% available time
#availabe time is calculated ad 8 hours

#AVAILABLE TIME
    c= '08:00:00'
    convert_into_time=datetime.strptime(c,'%H:%M:%S')
    struct_time= convert_into_time.utctimetuple()
    AVAILABLE_TIME=abs(calendar.timegm(struct_time)/1296000000 +6.2955555555555 + 3.415555555555)

#UNPLANNED DOWNTIME
    actual_duration = product_log.objects.filter(machine=request.a).aggregate(num=Sum('duration')).get("num")
    Unplanned_Downtime=AVAILABLE_TIME - actual_duration

#AVAILABLITY
    Availablity=(AVAILABLE_TIME - Unplanned_Downtime)*AVAILABLE_TIME

#performence=Ideal cycle time * Actual output * 100%(Available operting time)
# IDEAL_CYCLE_TIME=Actual duration / total product count(time taken to produce 1 part)

    total_bad_products=product_log.objects.filter(machine=request.a).aggregate(num=Sum('bad_product')).get("num")
    total_good_product=product_log.objects.filter(machine=request.a).aggregate(num=Sum('good_products')).get("num")
    total_product=total_bad_products + total_good_product
    ideal_cycle_time=total_product / actual_duration
#Available_operating_time=ideal cycle time * no of products
    available_operating_time=ideal_cycle_time *  total_product

#PERFORMENCE

    performrnce=(ideal_cycle_time * total_product) * available_operating_time

#QUALTY=no of good product * 100%( total product)
    quality=total_good_product * total_product

#OEE_ADDING
    Oee=Availablity * performrnce * quality
    oee.objects.create(machine_name=request.a,machine_OEE=Oee)
    return redirect(machine_s)




































































