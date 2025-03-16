from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
 
class  CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todoList')

    

class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todoList')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todoList')
        return super(RegisterPage, self).get(*args, **kwargs)




class todoList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/todoList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(completed = False)
        return context

class viewTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/viewTask.html'

class addTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description', 'completed']
    success_url = reverse_lazy('todoList')
    template_name = 'base/addTask.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addTask, self).form_valid(form)


class updateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = fields = ['title','description', 'completed']
    success_url = reverse_lazy('todoList')
    template_name = 'base/updateTask.html'

class deleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todoList')
    template_name = 'base/deleteTask.html'