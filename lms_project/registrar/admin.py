from django.contrib import admin

## Special Thanks:
## http://www.djangobook.com/en/2.0/chapter06.html
#
from registrar.models import FileUpload
from registrar.models import Course
from registrar.models import CourseSubmission
from registrar.models import CourseDiscussionPost
from registrar.models import CourseDiscussionThread
from registrar.models import CourseSetting
from registrar.models import CourseFinalMark
from registrar.models import Announcement
from registrar.models import Syllabus
from registrar.models import Policy
from registrar.models import Lecture
from registrar.models import Assignment
from registrar.models import AssignmentSubmission
from registrar.models import Exam
from registrar.models import ExamSubmission
from registrar.models import Quiz
from registrar.models import QuizSubmission
from registrar.models import EssayQuestion
from registrar.models import EssaySubmission
from registrar.models import MultipleChoiceQuestion
from registrar.models import MultipleChoiceSubmission
from registrar.models import TrueFalseQuestion
from registrar.models import TrueFalseSubmission
from registrar.models import ResponseQuestion
from registrar.models import ResponseSubmission
from registrar.models import PeerReview
from account.models import Student
from django.contrib.auth import get_permission_codename
from django.core.exceptions import (
    FieldDoesNotExist, FieldError, PermissionDenied, ValidationError,
)

admin.site.register(FileUpload)


class CourseAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(students__company__name=student_obj.company.name)
            except:
                return queryset
        return queryset

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseSubmission)
admin.site.register(CourseDiscussionPost)
admin.site.register(CourseDiscussionThread)
admin.site.register(CourseSetting)


class CourseFinalMarkAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(students__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset

admin.site.register(CourseFinalMark, CourseFinalMarkAdmin)
admin.site.register(Announcement)
admin.site.register(Syllabus)
admin.site.register(Policy)
admin.site.register(Lecture)
admin.site.register(Assignment)


class AssignmentSubmissionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        print("hello")
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(student__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset
admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)
admin.site.register(Exam)

class ExamSubmissionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(student__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset

admin.site.register(ExamSubmission, ExamSubmissionAdmin)
admin.site.register(Quiz)


class QuizSubmissionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(student__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset
admin.site.register(QuizSubmission, QuizSubmissionAdmin)
admin.site.register(PeerReview)
admin.site.register(EssayQuestion)


class EssaySubmissionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(student__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset
admin.site.register(EssaySubmission, EssaySubmissionAdmin)
admin.site.register(MultipleChoiceQuestion)


class MultipleChoiceSubmissionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(student__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset
admin.site.register(MultipleChoiceSubmission, MultipleChoiceSubmissionAdmin)
admin.site.register(TrueFalseQuestion)


class TrueFalseSubmissionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        student_obj = Student.objects.filter(user=request.user)
        if student_obj:
            student_obj = student_obj[0]
            try:
                return queryset.filter(student__company__name=student_obj.company.name)
            except:
                return queryset.filter(id=0)
        return queryset
admin.site.register(TrueFalseSubmission, TrueFalseSubmissionAdmin)
admin.site.register(ResponseQuestion)


class ResponseSubmissionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
            queryset = super().get_queryset(request)
            student_obj = Student.objects.filter(user=request.user)
            if student_obj:
                student_obj = student_obj[0]
                try:
                    return queryset.filter(students__company__name=student_obj.company.name)
                except:
                    return queryset.filter(id=0)
            return queryset
admin.site.register(ResponseSubmission)
