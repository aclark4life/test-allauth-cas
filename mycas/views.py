from django.shortcuts import render

# Create your views here.

from allauth_cas.views import CASAdapter

from .providers import MyCASProvider


class MyCASAdapter(CASAdapter):
    provider_id = MyCASProvider.id
    url = 'https://mycas.mydomain.net'  # The CAS server url
    version = 3  # Select the CAS protocol version used by the CAS server: 1, 2, 3…
