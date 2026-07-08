from django.urls import path
from . import views

urlpatterns = [
    path("visitors/", views.visitor_list, name="visitor_list"),
    path("visitors/add/", views.add_visitor, name="add_visitor"),

    path("departments/", views.department_list, name="department_list"),
    path("departments/add/", views.add_department, name="add_department"),

    path("persons/", views.person_list, name="person_list"),
    path("persons/add/", views.add_person, name="add_person"),

    path("visit-logs/", views.visitlog_list, name="visitlog_list"),
    path("visit-logs/add/", views.add_visitlog, name="add_visitlog"),
]