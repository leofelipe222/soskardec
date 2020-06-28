from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session

class OneSessionPerUSer:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.is_authenticated:
            current_sesstion_key = request.user.logged_in_user.session_key
            
            # compares user session key with the current session key in the browser
            if current_sesstion_key and current_sesstion_key != request.session.session_key:
                
                # Deletes the existing session key
                Session.objects.get(session_key=current_sesstion_key).delete()
            
            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
