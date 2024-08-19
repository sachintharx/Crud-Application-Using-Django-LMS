from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('fullname','mobile','student_id','grade')
        labels = {
            'fullname':'Full Name',
            'student_id':'Student ID'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        # self.fields['grade'].empty_label = "Select"
        self.fields['student_id'].required = False 
  
  
 
 
 
 
 
  
# from django import forms
# from .models import Student, Grade


# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student
#         fields = ('fullname','mobile','student_id','grade')
#         labels = {
#             'fullname':'Full Name',
#             'student_id':'Student ID'
#         }

#     def __init__(self, *args, **kwargs):
#         super(StudentForm,self).__init__(*args, **kwargs)
#         # self.fields['grade'].empty_label = "Select"
#         self.fields['student_id'].required = False