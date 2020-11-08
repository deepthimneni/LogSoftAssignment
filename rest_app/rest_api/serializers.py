from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    manager_name = serializers.CharField(
        source='manager.name',
        read_only=True
    )
    class Meta:
        model = Employee
        fields = ('id', 'name', 'manager_name')
