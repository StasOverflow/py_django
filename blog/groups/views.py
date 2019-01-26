from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
from .models import Group
from .models import Membership
from django.http import JsonResponse


def index(request):
    params = request.GET.dict()
    group_name = ''
    out_string = ''
    if 'group_name' in params:
        group_name = params['group_name']
        out_string = 'Got one'
    else:
        out_string = str(params)
    if group_name != '':
        out_string = group_name

    groups = Group.objects.all()
    print(groups[1].name)

    print(out_string)
    print(group_name)
    persons = list(Person.objects.filter(Membership__group_id__name=group_name).values())

    return JsonResponse(persons, safe=False)

# Create your views here.
