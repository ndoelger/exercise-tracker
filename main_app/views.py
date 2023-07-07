from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Exercise


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ExerciseIndex(ListView):
    model = Exercise
    template_name = 'exercises/index.html'
    context_object_name = 'exercises'

# class ExerciseDetails(DetailView):
#     model = Exercise
#     template_name = 'exercises/details.html'
#     context_object_name = 'exercises'

# class ExerciseCreate(CreateView):
#     model = Exercise
#     fields = '__all__'

# class ExerciseUpdate(UpdateView):
#     model = Exercise
#     fields = '__all__'

# class ExerciseDelete(DeleteView):
#   model = Exercise
#   success_url = '/exercises'