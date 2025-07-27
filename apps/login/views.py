from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm


class LoginView(View):
    template_name = 'login/base.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todo:dashboard')
        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('todo:dashboard')
        return render(request, self.template_name, {'form': form, 'invalid': True})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login:login')
