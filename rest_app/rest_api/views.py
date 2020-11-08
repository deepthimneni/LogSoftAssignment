from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee

# Create your views here.
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    print(employees)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)