from django.urls import path
from . import views

urlpatterns = [
    path("visitors/", views.visitor_list, name="visitor_list"),
    path("visitors/add/", views.add_visitor, name="add_visitor"),
    path("visitors/edit/<int:visitor_id>/", views.edit_visitor, name="edit_visitor"),
    path("visitors/delete/<int:visitor_id>/", views.delete_visitor, name="delete_visitor"),

    path("departments/", views.department_list, name="department_list"),
    path("departments/add/", views.add_department, name="add_department"),
    path("departments/edit/<int:department_id>/", views.edit_department, name="edit_department"),
    path("departments/delete/<int:department_id>/", views.delete_department, name="delete_department"),

    path("persons/", views.person_list, name="person_list"),
    path("persons/add/", views.add_person, name="add_person"),
    path("persons/edit/<int:person_id>/", views.edit_person, name="edit_person"),
    path("persons/delete/<int:person_id>/", views.delete_person, name="delete_person"),

    path("visit-logs/", views.visitlog_list, name="visitlog_list"),
    path("visit-logs/add/", views.add_visitlog, name="add_visitlog"),
    path("visit-logs/edit/<int:log_id>/", views.edit_visitlog, name="edit_visitlog"),
    path("visit-logs/delete/<int:log_id>/", views.delete_visitlog, name="delete_visitlog"),
]