from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from .permissions import AccountantOrHeadPermissionMixin

# Create your views here.


class HomePageView(TemplateView):

    template_name = "core/home.html"


class OrderDetailView(DetailView, LoginRequiredMixin):

    model = Order


class OrderView(LoginRequiredMixin, CreateView):

    template_name = "core/order.html"
    model = Order
    fields = ['name', 'amount', 'material']

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class OrderListView(ListView):

    model = Order

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)


class AccountantBaseView(TemplateView, AccountantOrHeadPermissionMixin):
    template_name = "core/accountant_base.html"


class AccountantOrderListView(ListView, AccountantOrHeadPermissionMixin):
    model = Order
    template_name = "core/accountant_list.html"


class AccountantOrderDetailView(DetailView, AccountantOrHeadPermissionMixin):
    model = Order
    template_name = "core/accountant_detail.html"
