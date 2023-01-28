from rest_framework import serializers
from .models import Student, Subject, Teacher, SubjectStudentMap

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectStudentMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectStudentMap
        fields = '__all__'
