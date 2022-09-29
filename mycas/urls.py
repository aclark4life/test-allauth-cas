from allauth_cas.urls import default_urlpatterns

from .provider import MyCASProvider

urlpatterns = default_urlpatterns(MyCasProvider)
