from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Exercise
from .forms import CompletionForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class ExerciseIndex(ListView):
    model = Exercise
    template_name = 'exercises/index.html'
    context_object_name = 'exercises'


def exercise_details(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    completion_form = CompletionForm()
    return render(request, 'exercises/details.html', {
        'exercise': exercise, 'completion_form': completion_form
    })


class ExerciseCreate(CreateView):
    model = Exercise
    fields = '__all__'


class ExerciseUpdate(UpdateView):
    model = Exercise
    fields = '__all__'


class ExerciseDelete(DeleteView):
    model = Exercise
    success_url = '/exercises'

def add_completion(request, exercise_id):
    form = CompletionForm(request.POST)
    if form.is_valid():
        new_completion = form.save(commit=False)
        new_completion.exercise_id = exercise_id
        new_completion.save()
    return redirect('exercise_details', exercise_id=exercise_id)