from django.db import models

class Visitor(models.Model):
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField()
    purpose = models.CharField(max_length=100)
    person_to_visit = models.CharField(max_length=100)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        default="Inside"
    )

    def __str__(self):
        return self.full_name