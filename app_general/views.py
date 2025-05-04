from django.http.response import HttpResponse
from django.shortcuts import render
from app_foods.models import Food
# Create your views here.
def home(request):
    recommended_foods = Food.objects.filter(recommend=True)[:3]
    return render(request, 'app_general/home.html', {
        'recommended_foods' : recommended_foods,
    })