from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExerciseIndex.as_view(), name="home"),
    path('about/', views.about, name='about'),
    path('exercises/', views.ExerciseIndex.as_view(), name='exercises_index'),
    path('exercises/<int:pk>/details/', views.ExerciseDetails.as_view(), name='exercise_details'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercise_create'),
    path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercise_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercise_delete'),
]

