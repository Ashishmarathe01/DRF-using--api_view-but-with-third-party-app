from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework. response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','DELETE','PUT','PATCH'])
def student_api(request):
    # for id base operaton
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)# convert it in native python data
            return Response(serializer.data) # data is varibale were serializer is store it will convert it into json and send response
        stu=Student.objects.all() # if id is not given then it will excute
        serializer=StudentSerializer(stu,many=True) # many need to write bcoz its query set
        return Response(serializer.data)




    # Not: if you want for brower api you can remove id bcoz it getting from url we used third party app that we get id
    #
    # def student_api(request,id=None): only make this changes for browesr api
    #
    # if request.method == 'GET':
    #     id = id
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializer = StudentSerializer(stu)  # convert it in native python data
    #         return Response(
    #             serializer.data)  # data is varibale were serializer is store it will convert it into json and send response
    #     stu = Student.objects.all()  # if id is not given then it will excute
    #     serializer = StudentSerializer(stu, many=True)  # many need to write bcoz its query set
    #     return Response(serializer.data)



    # for post
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data) # it will make it complex qury
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors) # it will give nonfield erroe

    #for put
    if  request.method=='PUT':
        id=request.data.get('id') # get id for delet
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete done put request'})
        return Response(serializer.errors)

    # partiall update
    if  request.method=='PUT':
        id=request.data.get('id') # get id for delet
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)# partuall write for partially upadte
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partially done put request'})
        return Response(serializer.errors)


    # for deelet
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'deeletd data '})

