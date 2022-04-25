from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from book.models import PeopleInfo, BookInfo

BookInfo.objects.create(
    name='三国演义'

)

PeopleInfo.objects.create(
    name='刘备',
    book_id='5'
)
PeopleInfo.objects.create(
    name='关羽',
    book_id=5
)


def index(request):
    return HttpResponse("OK")
