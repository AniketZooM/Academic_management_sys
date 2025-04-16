from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import CustomUser, Student, Teacher, HomeWork, MakeBatch, Question, Answer, ApplyForLeave, NoticeForStudent
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm

class CommonRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'phone_number', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form__input', 'placeholder': 'Enter your email'})
        self.fields['email'].label = 'Email'
        self.fields['phone_number'].widget.attrs.update({'class': 'form__input', 'placeholder': 'Enter your phone number'})
        self.fields['phone_number'].label = 'Phone Number'

        self.fields['password1'].widget.attrs.update({'class': 'form__input', 'placeholder': 'Set your password'})
        self.fields['password1'].label = 'Password'

        self.fields['password2'].widget.attrs.update({'class': 'form__input', 'placeholder': 'Confirm your password'})
        self.fields['password2'].label = 'Confirm Password'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            's_name', 'class_subjects', 'guardian_phone', 's_phone', 'guardian_email', 'shift',
        )   

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        placeholders = {
            's_name': 'Enter full name of student',
            'class_subjects': 'Select the class you will be admitted to *',
            'guardian_phone': 'Guardian\'s mobile number (Required) *',
            's_phone': 'Your mobile number (Optional)',
            'guardian_email': 'Guardian\'s email (Optional)',
            'shift': 'Select the shift you will be admitted to *',
        }

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form__input'
            self.fields[field_name].widget.attrs['placeholder'] = placeholders[field_name]

    def clean_guardian_phone(self):
        guardian_phone = self.cleaned_data.get('guardian_phone')
        if not guardian_phone.isdigit():
            raise ValidationError('Guardian phone number should only contain digits.')
        return guardian_phone
    
    def clean_s_name(self):
        s_name = self.cleaned_data.get('s_name')
        if s_name is None:
            raise ValidationError('This field cannot be empty')
        return s_name
    
    def clean_class_subjects(self):
        class_subjects = self.cleaned_data.get('class_subjects')
        if class_subjects is None:
            raise ValidationError('Please select a class')
        return class_subjects
    
    def clean_s_phone(self):
        s_phone = self.cleaned_data.get('s_phone')
        if s_phone and not s_phone.isdigit():
            raise ValidationError('Phone number should only contain digits.')     
        return s_phone
    
    def clean_guardian_email(self):
        guardian_email = self.cleaned_data.get('guardian_email')
        return guardian_email
    
    def clean_shift(self):
        shift = self.cleaned_data.get('shift')
        if shift is None:
            raise ValidationError('Please select a shift')
        return shift


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = (
            't_name', 't_present_adress', 't_permnt_adress', 't_extra_phone',
        )

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        placeholders = {
            't_name': 'Enter full name',
            't_present_adress': 'Present address *',
            't_permnt_adress': 'Permanent address *',
            't_extra_phone': 'Mobile number (Optional)',
        }
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form__input'
            self.fields[field_name].widget.attrs['placeholder'] = placeholders[field_name]
    
    def clean_t_name(self):
        t_name = self.cleaned_data.get('t_name')
        if not t_name:
            raise ValidationError('Sorry! This field cannot be left empty!')
        return t_name
    
    def clean_t_present_adress(self):
        t_present_adress = self.cleaned_data.get('t_present_adress')
        if not t_present_adress:
            raise ValidationError('Sorry! This field cannot be left empty!')
        return t_present_adress
    
    def clean_t_permnt_adress(self):
        t_permnt_adress = self.cleaned_data.get('t_permnt_adress')
        if not t_permnt_adress:
            raise ValidationError('Sorry! This field cannot be left empty!')
        return t_permnt_adress
    
    def clean_t_extra_phone(self):
        t_extra_phone = self.cleaned_data.get('t_extra_phone')
        if t_extra_phone and not t_extra_phone.isdigit():
            raise ValidationError('Mobile number should only contain digits.')
        return t_extra_phone

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['t_name', 'profile_pic', 'teacher_background', 't_present_adress', 't_permnt_adress', 't_extra_phone']
        labels = {
            't_name': 'Full Name',
            'profile_pic': 'Your Picture',
            'teacher_background': 'Background',
            't_present_adress': 'Present Address',
            't_permnt_adress': 'Permanent Address',
            't_extra_phone': 'Additional Mobile Number',
        }

    def __init__(self, *args, **kwargs):
        super(TeacherProfileForm, self).__init__(*args, **kwargs)

        placeholders = {
            't_name': 'Full Name',
            'profile_pic': 'Your Picture',
            'teacher_background': 'Background',
            't_present_adress': 'Present Address',
            't_permnt_adress': 'Permanent Address',
            't_extra_phone': 'Additional Mobile Number',
        }

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'
            self.fields[field_name].widget.attrs['placeholder'] = placeholders[field_name]


class PassChangeForm(BasePasswordChangeForm):
    class Meta:
        model = CustomUser 
        fields = ['old_password', 'new_password1', 'new_password2']
    
    def __init__(self, *args, **kwargs):
        super(PassChangeForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            's_name',
            's_phone',
            'guardian_email',
            'profile_pic',
        ]

        labels = {
            's_name': 'Full Name',
            'profile_pic': 'Your Picture',
            's_id': 'Your ID',
            's_phone': 'Your Mobile Number',
        }

    def __init__(self, *args, **kwargs):
        super(StudentEditForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'


class HomeWorkForm(forms.ModelForm):
    last_day_of_submit = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    class Meta:
        model = HomeWork
        fields = ['title', 'hw_detail', 'last_day_of_submit', 'for_class', 'batch', 'subject']

    def __init__(self, *args, **kwargs):
        super(HomeWorkForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'

        self.fields['last_day_of_submit'].widget.attrs['placeholder'] = "Ex: 2023-11-12"


from users.models import NoteAndSheet

class NoteAndSheetForm(forms.ModelForm):
    class Meta:
        model = NoteAndSheet
        fields = ['title', 'for_class', 'batch', 'subject', 'upload_note']

    def __init__(self, *args, **kwargs):
        super(NoteAndSheetForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['ques_name', 'mark', 'how_many_answer_for_this_ques']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct']

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'


class ApplyLeaveForm(forms.ModelForm):
    attachment = forms.FileField(
        widget=forms.FileInput(attrs={'required': False})
    )
    
    class Meta:
        model = ApplyForLeave
        fields = ['reason_for_apply', 'description', 'attachment']

    def __init__(self, *args, **kwargs):
        super(ApplyLeaveForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input-field'
