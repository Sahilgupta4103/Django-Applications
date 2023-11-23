from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serailizers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    #complanies/companyID/employees -> to get employess from specific company
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emps_serial = EmployeeSerializer(emps,many=True,context={'request':request})
        return Response(emps_serial.data)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer    