from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib import messages



class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html' # ту просто задаємо всі дані для форми
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        for fields, errors in form.errors.items():
            for error in errors:
                messages.warning(self.request, error)# попросити поясниити
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# просто записуємо в контекст title
        context['title'] = 'Register'
        return context