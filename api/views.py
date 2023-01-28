from .models import Student, Subject, Teacher, SubjectStudentMap
from .serializers import StudentSerializer, SubjectSerializer, TeacherSerializer, SubjectStudentMapSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_subject(request):
    if request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_teacher(request):
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def enroll_student(request, student_id, subject_id):
    if request.method == 'POST':
        try:
            stu = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"Error":"student id does not exist"},status=status.HTTP_404_NOT_FOUND)

        try:
            sub = Subject.objects.get(pk=subject_id)
        except Subject.DoesNotExist:
            return Response({"Error":"subject id does not exist"},status=status.HTTP_404_NOT_FOUND)

        data = {}
        data["student_id"] = stu.id
        data["subject_id"] = sub.id
        serializer = SubjectStudentMapSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_teachers(request, student_id):
    if request.method == 'GET':
        try:
            sub = SubjectStudentMap.objects.filter(student_id=student_id)
            tea = Teacher.objects.filter(subject_id__in=sub.values_list('subject_id', flat=True).distinct())
            serializer = TeacherSerializer(tea, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Student.DoesNotExist:
            return Response({"Error":"student id does not exist"},status=status.HTTP_404_NOT_FOUND)

        
