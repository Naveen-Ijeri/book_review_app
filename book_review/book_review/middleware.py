
from django.utils.deprecation import MiddlewareMixin
from auth_app.models import UserSessions
from datetime import datetime, timedelta, timezone


class RequestLoggingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        now = datetime.now(timezone.utc)
        request.is_token_valid = False
        token = request.META.get('HTTP_TOKEN')
        if token:
            session = UserSessions.objects.filter(token=token).first()
            idle_timeout = 1  #Token is valid only for 10 minutes
            if session:
                if now > session.created_at + timedelta(minutes=idle_timeout):
                    request.is_token_valid = False
                else:
                    request.user_id = session.user_id
                    request.username = session.username
                    request.email = session.email
                    request.is_token_valid = True
