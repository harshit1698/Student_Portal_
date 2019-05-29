from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from std.models import Student, StdForm


class Userregister(CreateView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login",)


class CBV(ListView):
    model = Student
    template_name = 'Test_Cases.html'
    context_object_name = "Yo_Boy"


class GeT(DetailView):
    model = Student
    template_name = 'd1.html'
    queryset = Student.objects.all()


class Create(CreateView):
    form_class = StdForm
    template_name = '1yo.html'
    queryset = Student.objects.all()
    success_url = reverse_lazy('fb:welcome')


class Update(UpdateView):
    template_name = 'yo2.html'
    fields = ['name']
    # form_class = TestModel
    queryset = Student.objects.all()
    success_url = reverse_lazy("fb:welcome")


class Delete(DeleteView):
    template_name = 'yo3.html'
    model = Student
    success_url = reverse_lazy('fb:welcome')


def welc(request):
    obj=Student.objects.all()
    return render(request,'Welcome.html',{"obj":obj})


