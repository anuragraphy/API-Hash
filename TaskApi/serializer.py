from rest_framework import serializers
from .models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
        read_only_fields = ['average','user']

    def create(self, validated_data):
        read_only_fields = ['average','user']

        for field in read_only_fields:
            if field in self.initial_data:
                raise serializers.ValidationError(f"{field} field is read-only and cannot be modified.")

        average = self.calculate_average(validated_data)
        validated_data['average'] = average
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        read_only_fields = ['average','user']

        for field in read_only_fields:
            if field in self.initial_data:
                raise serializers.ValidationError(f"{field} field is read-only and cannot be modified.")

        average = self.calculate_average(validated_data)
        validated_data['average'] = average
        validated_data['user'] = self.context['request'].user
        return super().update(instance, validated_data)
    
    def calculate_average(self, validated_data):
        impact = validated_data['impact']
        confidence = validated_data['confidence']
        ease = validated_data['ease']
        

        return (impact + confidence + ease) / 3

class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['taskName']
        