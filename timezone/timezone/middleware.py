from backports import zoneinfo
from django.conf import settings

from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
            settings.CITY=request.session.get('django_timezone_city')
        else:
            timezone.deactivate()
        return self.get_response(request)