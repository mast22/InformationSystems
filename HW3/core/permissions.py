from users.models import CustomUser
from django.http import HttpResponseForbidden


class AccountantOrHeadPermissionMixin:

    def has_permissions(self):
        return self.request.user.role == 'accountant' or self.request.user.role == 'head'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise HttpResponseForbidden('You do not have permission.')
        return super(AccountantOrHeadPermissionMixin, self).dispatch(
            request, *args, **kwargs)
