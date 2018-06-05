from django.shortcuts import render

# Create your views here.
def golfer_list(request):
    return render(request, 'handicaps/golfer_list.html', {})
