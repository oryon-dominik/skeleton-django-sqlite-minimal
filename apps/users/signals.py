from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    """Do something with loggedin users"""
    pass
