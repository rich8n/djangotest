from django.shortcuts import render
from.models import Golfer

# Create your views here.
def golfer_list(request):
    golfers = Golfer.objects.filter(status__in=['Team','Substitute']).order_by('last', 'first')
    return render(request, 'handicaps/golfer_list.html', {'golfers': golfers})

def home(request):
    golfers = Golfer.objects.filter(status__in=['Team','Substitute']).order_by('last', 'first')
    return render(request, 'handicaps/home.html',{'golfers': golfers})
