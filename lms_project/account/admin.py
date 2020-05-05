from django.contrib import admin
from account.models import PrivateMessage
from account.models import Student
from account.models import Teacher

admin.site.register(PrivateMessage)


class StudentAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
            queryset = super().get_queryset(request)
            student_obj = Student.objects.filter(user=request.user)
            if student_obj:
                student_obj = student_obj[0]
                try:
                    return queryset.filter(company=student_obj.company)
                except:
                    return queryset.filter(id=0)
            return queryset

admin.site.register(Student)
admin.site.register(Teacher)
