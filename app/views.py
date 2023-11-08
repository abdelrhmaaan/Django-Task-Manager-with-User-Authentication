# from django.http import 
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView , DetailView , UpdateView , DeleteView
from app.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        # print(Task.objects.filter(user=request.user))
        # print(request.user)
        # print(tasks)
    context = {'object_list':tasks}
    print(tasks)
    return render(request,'app/index.html',context)


class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title']
    # template_name = 'app/index.html'
    # tasks = Task.objects.all()
    # context = {'tasks':tasks}
    # queryset = tasks
    success_url = reverse_lazy('home')

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        print(context)
        return context


class TaskDetial(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    # template_name = '' # u can change the template name not strict !!

class UpdateTask(UpdateView):
    model = Task
    template_name = 'app/task_update.html'
    context_object_name ='task'
    fields = ['title']
    success_url = reverse_lazy('home')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('home')