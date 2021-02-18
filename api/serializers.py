from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Workout, Exercise

class UserSerializer(serializers.HyperlinkedModelSerializer):
    workouts = serializers.HyperlinkedRelatedField(many=True, view_name='workout-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'workouts']

class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Workout` instance, given the validated data.
        """
        return Workout.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Workout` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        return instance

    class Meta:
        model = Workout
        fields = ['url', 'id', 'name', 'owner']

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    class Meta:
        model = Exercise
        fields = ['url', 'id', 'name']