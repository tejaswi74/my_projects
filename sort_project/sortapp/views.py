from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random

def insert_rows(request):
    fake = Faker()
    for _ in range(50):
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18, 80),
            email=fake.email()
        )
    return HttpResponse("50 records inserted successfully.")

def person_list(request):
    sort_by = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')

    if order == "desc":
        sort_by = f"-{sort_by}"

    persons = Person.objects.all().order_by(sort_by) if sort_by else Person.objects.all()
    
    return render(request, 'sortapp/person_list.html', {'persons': persons, 'sort_by': sort_by, 'order': order})

def index(request):
    return HttpResponse("Hello!!")