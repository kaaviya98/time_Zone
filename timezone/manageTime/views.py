from django.shortcuts import redirect, render
from django.utils import timezone
from django.urls import reverse
from django.conf import settings


common_timezones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Chennai':'Asia/Kolkata',
   
}

def display(request):
   
    return render(request, 'display.html', {"time":timezone.now(),"city":settings.CITY})

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        request.session['django_timezone_city'] = get_city( request.POST['timezone'])
        
        return redirect(reverse('manageTime:display'))
    else:
        return render(request, 'template.html', {'timezones': common_timezones.items(),})

def get_city(timezone):
    for city,zone in common_timezones.items():
        if zone==timezone:
            return city
