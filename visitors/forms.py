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
            "person_to_visit",
            "purpose",
        ]

        widgets = {
            "purpose": forms.TextInput(attrs={
                "placeholder": "Example: Payment, meeting, inquiry, delivery"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        visitor = cleaned_data.get("visitor")

        if visitor:
            existing_log = VisitLog.objects.filter(
                visitor=visitor,
                status="Inside"
            )

            if self.instance and self.instance.pk:
                existing_log = existing_log.exclude(pk=self.instance.pk)

            if existing_log.exists():
                raise forms.ValidationError(
                    "This visitor is already checked in and has not checked out yet."
                )

        return cleaned_data