from allauth.socialaccount.providers.base import ProviderAccount
from allauth_cas.providers import CASProvider


class MyCASAccount(ProviderAccount):
    pass


class MyCASProvider(CASProvider):
    id = 'mycas'  # Choose an identifier for your provider
    name = 'My CAS'  # Verbose name of your provider
    account_class = MyCASAccount


provider_classes = [MyCASProvider]
