from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'due_date', 'owner']
        read_only_fields = ['id', 'created_at', 'owner']

    def validate_status(self, value):
        allowed = {'pendente', 'em_andamento', 'concluida'}
        if value not in allowed:
            raise serializers.ValidationError('Status inválido.')
        return value