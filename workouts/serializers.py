from rest_framework import serializers
from .models import Exercise, RoutineExercise, WorkOutRoutine

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description']

class RoutineExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineExercise
        fields = ['id', 'exercise', 'order']
        
        
class RoutineSerializer(serializers.ModelSerializer):
        # many=True означает, что упражнений внутри рутины может быть несколько (список)
        routine_exercises = RoutineExerciseSerializer(many=True, read_only=True)
        
        class Meta:
            model = WorkOutRoutine
            fields = ['id', 'user', 'title', 'notes', 'routine_exercises']
    
class ExerciseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id','name', 'description', 'user', 'is_custom']
        read_only_fields = ['user', 'is_custom']
