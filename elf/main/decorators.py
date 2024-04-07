# accounts/decorators.py
from django.shortcuts import redirect
from functools import wraps
from .models import Organization

def organization_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if isinstance(request.user, Organization):
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'unauthorized_access.html')
        else:
            return redirect('organization_login')

    return _wrapped_view
