from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Visitor, Department, PersonToVisit, VisitLog
from .forms import VisitorForm, DepartmentForm, PersonToVisitForm, VisitLogForm


@login_required(login_url="login")
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, "visitor_list.html", {"visitors": visitors})


@login_required(login_url="login")
def add_visitor(request):
    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Visitor added successfully.")
            return redirect("visitor_list")

    else:
        form = VisitorForm()

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Add Visitor"
    })


@login_required(login_url="login")
def department_list(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {"departments": departments})


@login_required(login_url="login")
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Department added successfully.")
            return redirect("department_list")

    else:
        form = DepartmentForm()

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Add Department"
    })


@login_required(login_url="login")
def person_list(request):
    persons = PersonToVisit.objects.all()
    return render(request, "person_list.html", {"persons": persons})


@login_required(login_url="login")
def add_person(request):
    if request.method == "POST":
        form = PersonToVisitForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Person to visit added successfully.")
            return redirect("person_list")

    else:
        form = PersonToVisitForm()

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Add Person to Visit"
    })


@login_required(login_url="login")
def visitlog_list(request):
    logs = VisitLog.objects.all()
    return render(request, "visitlog_list.html", {"logs": logs})


@login_required(login_url="login")
def add_visitlog(request):
    if request.method == "POST":
        form = VisitLogForm(request.POST)

        if form.is_valid():
            visitlog = form.save(commit=False)

            # This connects the logged-in staff/user to the visit log
            visitlog.user = request.user

            visitlog.save()
            messages.success(request, "Visit log added successfully.")
            return redirect("visitlog_list")

    else:
        form = VisitLogForm()

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Add Visit Log"
    })  