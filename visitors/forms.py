from django import forms
from .models import Visitor, Department, PersonToVisit, VisitLog


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            "full_name",
            "contact_number",
            "email",
            "address",
        ]


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "department_name",
            "office_location",
        ]


class PersonToVisitForm(forms.ModelForm):
    class Meta:
        model = PersonToVisit
        fields = [
            "full_name",
            "position",
            "department",
        ]


class VisitLogForm(forms.ModelForm):
    class Meta:
        model = VisitLog
        fields = [
            "visitor",
            "department",
            "purpose",
            "check_out_time",
            "status",
        ]

        widgets = {
            "purpose": forms.TextInput(attrs={
                "placeholder": "Example: Meeting, interview, delivery"
            }),
            "check_out_time": forms.TimeInput(attrs={
                "type": "time"
            }),
        }