from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import User, Order
from .forms import OrderForm, ProfileForm

class IndexCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'homepage/index.html'
    success_url = reverse_lazy('homepage:index') 

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "Пожалуйста, войдите в систему, чтобы создать заказ.")
            return redirect('login')
        form.instance.creator = self.request.user
        messages.success(self.request, "Заказ успешно создан!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка при заполнении формы. Пожалуйста, проверьте данные.")
        return super().form_invalid(form)

class ProfileListView(ListView):
    model = Order
    template_name = 'homepage/profile.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self): 
        self.profile = get_object_or_404(User, username=self.kwargs['username'])
        if self.request.user == self.profile:
            return Order.objects.filter(creator=self.profile).order_by('-created_at')
        return Order.objects.none()

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'homepage/update_order.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage:profile', kwargs={'username': self.request.user.username})

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.creator

    def form_valid(self, form):
        messages.success(self.request, "Заказ успешно обновлен!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка при заполнении формы. Пожалуйста, проверьте данные.")
        return super().form_invalid(form)

class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'homepage/order_confirm_delete.html'

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.creator

    def get_success_url(self):
        messages.success(self.request, "Заказ успешно удален!")
        return reverse_lazy('homepage:profile', kwargs={'username': self.request.user.username})