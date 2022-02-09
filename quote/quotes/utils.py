

from django.contrib.auth.mixins import AccessMixin

from django.shortcuts import redirect
from django.urls import reverse

# Chgitem es bolor depqerum normal kashxati
class NotLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            return redirect(reverse('quote:quote-list'))
        return super().dispatch(request, *args, **kwargs)

