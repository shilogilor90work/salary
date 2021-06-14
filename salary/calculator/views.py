from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from calculator.models import Salary
from decimal import Decimal


def salary(request):
    context = {}
    return render(request, 'salary.html', context)

@csrf_exempt
def current(request):
    context = {}
    return render(request, 'current.html', context)
    # return HttpResponse("<h1> current </h1>")

def compare(request):
    salaries = Salary.objects.all()
    context = {"salaries": salaries}
    return render(request, 'compare.html', context)

@csrf_exempt
@api_view(['POST'])
def update_salary(request):
    """Update salary
    updates the salary
        Arguments:
            request {Requset} -- Request object.

        Returns:
            Response -- Response object.
    """
    salary = Salary.objects.filter(name=request.POST.get('name'))
    if salary.exists():
        salary.salary = Decimal(request.POST.get('salary'))
        salary.salary_net = Decimal(request.POST.get('salary_net'))
        salary.day_hours = Decimal(request.POST.get('day_hours'))
        salary.vacation_days = Decimal(request.POST.get('vacation_days'))
        salary.travel_time = Decimal(request.POST.get('travel_time'))
        salary.sickdays_value = request.POST.get('sickdays_value')
        salary.pension = Decimal(request.POST.get('pension'))
        salary.pitzuim = Decimal(request.POST.get('pitzuim'))
        salary.hishtalmut = Decimal(request.POST.get('hishtalmut'))
        salary.nesiot_income = Decimal(request.POST.get('nesiot_income'))
        salary.gas_cost = Decimal(request.POST.get('gas_cost'))
        salary.lunch = Decimal(request.POST.get('lunch'))
        salary.holidays_like_friday = request.POST.get('holidays_like_friday')
        salary.chol_hamoed = Decimal(request.POST.get('chol_hamoed'))
        salary.minimum_hours = Decimal(request.POST.get('minimum_hours'))
        salary.parking = Decimal(request.POST.get('parking'))
        salary.flexable_hours = request.POST.get('flexable_hours')
        salary.minimum_hours_aday = Decimal(request.POST.get('minimum_hours_aday'))

        salary.save()
        return Response({"message": "salary was updated"})
    else:
        Salary.objects.create(name=request.POST.get('name'), salary=Decimal(request.POST.get('salary')), salary_net=Decimal(request.POST.get('salary_net')),
        day_hours=Decimal(request.POST.get('day_hours')),
        vacation_days=Decimal(request.POST.get('vacation_days')),
        travel_time=Decimal(request.POST.get('travel_time')),
        sickdays_value=request.POST.get('sickdays_value'),
        pension=Decimal(request.POST.get('pension')),
        pitzuim=Decimal(request.POST.get('pitzuim')),
        hishtalmut=Decimal(request.POST.get('hishtalmut')),
        nesiot_income=Decimal(request.POST.get('nesiot_income')),
        gas_cost=Decimal(request.POST.get('gas_cost')),
        holidays_like_friday=request.POST.get('holidays_like_friday'),
        chol_hamoed=Decimal(request.POST.get('chol_hamoed')),
        parking=Decimal(request.POST.get('parking')),
        flexable_hours=request.POST.get('flexable_hours'),
        minimum_hours_aday=Decimal(request.POST.get('minimum_hours_aday')))
    return Response({"message": "salary was created"})
