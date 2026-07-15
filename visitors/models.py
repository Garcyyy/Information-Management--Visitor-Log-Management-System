from django.db import models
from django.contrib.auth.models import User


class Visitor(models.Model):
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class PersonToVisit(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    # ForeignKey allows one department to have many persons
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="persons"
    )

    def __str__(self):
        return self.full_name


class VisitLog(models.Model):
    STATUS_CHOICES = (
        ("Inside", "Inside"),
        ("Exited", "Exited"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="visit_logs"
    )

    visitor = models.ForeignKey(
        Visitor,
        on_delete=models.CASCADE,
        related_name="visit_logs"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="visit_logs"
    )

    person_to_visit = models.ForeignKey(
        PersonToVisit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="visit_logs"
    )

    purpose = models.CharField(max_length=200)
    visit_date = models.DateField(auto_now_add=True)
    check_in_time = models.TimeField(auto_now_add=True)
    check_out_time = models.TimeField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Inside"
    )

    def __str__(self):
        return f"{self.visitor.full_name} - {self.department.department_name}"