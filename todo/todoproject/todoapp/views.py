from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import todo
from .forms import form1
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView, DeleteView


# this is to import the LIST view function


# Create your views here.
class taskdelete(DeleteView):
    model = todo
    template_name = 'delete.html'
    # success_url = reverse_lazy('cbvtodo')  any one we can use eithrt 18 or 19 command
    def get_success_url(self):
        return reverse_lazy('cbvtodo')

class taskupdate(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 'task3'
    fields = ['name', 'priority', 'date']

    # after editing to show the edited detail view need to create one url
    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class taskdetailview(DetailView):
    model = todo
    template_name = 'details.html'
    context_object_name = 'task'


class tasklistview(ListView):
    model = todo
    template_name = 'todo.html'
    context_object_name = 'todo3'


# it is working it will show ony the data if iam pressing submit it willl show error because no function
def demo(request):
    todo2 = todo.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')  # common code to get the data
        importance = request.POST.get('importance')
        date1 = request.POST.get('date')
        todo1 = todo(name=name, priority=importance,
                     date=date1)  # here we are assinging the varible to the model table data
        # todo1 is a variable name
        todo1.save()  # finally need to save then only it will save in admin panel
    return render(request, 'todo.html', {'todo3': todo2})


#     here 2 variables we created thats why we are taking 2 elements
def delete(request, taskid):
    if request.method == 'POST':
        todo4 = todo.objects.get(id=taskid)
        todo4.delete()
        return redirect("/")
    return render(request, "delete.html")


def edit(request, id):
    todo6 = todo.objects.get(id=id)
    todo7 = form1(request.POST or None, request.FILES, instance=todo6)
    if todo7.is_valid():
        todo7.save()
        return redirect('/')
    return render(request, "edit.html", {'todo7': todo7, 'todo6': todo6})
