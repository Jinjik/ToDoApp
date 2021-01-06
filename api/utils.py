from typing import Union

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication

from .models import Organization


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


def authenticate(email=None, organization=None, password=None) -> Union[None, User]:
    """Function for chec

    Args:
        email: User's email
        organization: User's organization for authorization
        password: User's password

    Returns:
        None or

    """
    user_model = get_user_model()

    try:
        user = user_model.objects.get(email=email)
        organization = Organization.objects.get(name=organization)
    except user_model.DoesNotExist:
        return None
    else:

        if organization in user.user.organization.all():

            if user.check_password(password):
                user.user.login = organization
                user.user.save()
                return user

    return None