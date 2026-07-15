from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Visitor, Department, PersonToVisit, VisitLog
from .forms import VisitorForm, DepartmentForm, PersonToVisitForm, VisitLogForm


# =========================
# VISITOR VIEWS
# =========================

@login_required(login_url="login")
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, "visitor_list.html", {
        "visitors": visitors
    })


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
def edit_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)

    if request.method == "POST":
        form = VisitorForm(request.POST, instance=visitor)

        if form.is_valid():
            form.save()
            messages.success(request, "Visitor updated successfully.")
            return redirect("visitor_list")
    else:
        form = VisitorForm(instance=visitor)

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Edit Visitor"
    })


@login_required(login_url="login")
def delete_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)

    if request.method == "POST":
        visitor.delete()
        messages.success(request, "Visitor deleted successfully.")
        return redirect("visitor_list")

    return render(request, "confirm_delete.html", {
        "object": visitor,
        "title": "Delete Visitor",
        "cancel_url": "visitor_list"
    })


# =========================
# DEPARTMENT VIEWS
# =========================

@login_required(login_url="login")
def department_list(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {
        "departments": departments
    })


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
def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully.")
            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Edit Department"
    })


@login_required(login_url="login")
def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == "POST":
        department.delete()
        messages.success(request, "Department deleted successfully.")
        return redirect("department_list")

    return render(request, "confirm_delete.html", {
        "object": department,
        "title": "Delete Department",
        "cancel_url": "department_list"
    })


# =========================
# PERSON TO VISIT VIEWS
# =========================

@login_required(login_url="login")
def person_list(request):
    persons = PersonToVisit.objects.select_related("department").all()
    return render(request, "person_list.html", {
        "persons": persons
    })


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
def edit_person(request, person_id):
    person = get_object_or_404(PersonToVisit, id=person_id)

    if request.method == "POST":
        form = PersonToVisitForm(request.POST, instance=person)

        if form.is_valid():
            form.save()
            messages.success(request, "Person to visit updated successfully.")
            return redirect("person_list")
    else:
        form = PersonToVisitForm(instance=person)

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Edit Person to Visit"
    })


@login_required(login_url="login")
def delete_person(request, person_id):
    person = get_object_or_404(PersonToVisit, id=person_id)

    if request.method == "POST":
        person.delete()
        messages.success(request, "Person to visit deleted successfully.")
        return redirect("person_list")

    return render(request, "confirm_delete.html", {
        "object": person,
        "title": "Delete Person to Visit",
        "cancel_url": "person_list"
    })


# =========================
# VISIT LOG VIEWS
# =========================

@login_required(login_url="login")
def checkout_visitlog(request, log_id):
    log = get_object_or_404(VisitLog, id=log_id)

    if request.method == "POST":
        next_url = request.POST.get("next") or "visitlog_list"

        if log.status == "Exited":
            messages.error(request, "This visitor has already checked out.")
        else:
            log.status = "Exited"
            log.check_out_time = timezone.localtime(timezone.now()).time()
            log.save()

            messages.success(request, "Visitor checked out successfully.")

        return redirect(next_url)

    return redirect("visitlog_list")

@login_required(login_url="login")
def visitlog_list(request):
    logs = VisitLog.objects.select_related(
        "visitor",
        "department",
        "user"
    ).order_by("-visit_date", "-check_in_time")

    return render(request, "visitlog_list.html", {
        "logs": logs
    })


@login_required(login_url="login")
def add_visitlog(request):
    next_url = (
        request.GET.get("next")
        or request.POST.get("next")
        or "visitlog_list"
    )

    if request.method == "POST":
        form = VisitLogForm(request.POST)

        if form.is_valid():
            visitlog = form.save(commit=False)

            # Automatically records the logged-in staff/user
            visitlog.user = request.user

            visitlog.save()

            messages.success(request, "Visit log added successfully.")
            return redirect(next_url)
    else:
        form = VisitLogForm()

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Add Visit Log",
        "next_url": next_url
    })


@login_required(login_url="login")
def edit_visitlog(request, log_id):
    log = get_object_or_404(VisitLog, id=log_id)

    next_url = (
        request.GET.get("next")
        or request.POST.get("next")
        or "visitlog_list"
    )

    if request.method == "POST":
        form = VisitLogForm(request.POST, instance=log)

        if form.is_valid():
            updated_log = form.save(commit=False)

            # Keeps the original staff/user who recorded the log
            updated_log.user = log.user

            updated_log.save()

            messages.success(request, "Visit log updated successfully.")
            return redirect(next_url)
    else:
        form = VisitLogForm(instance=log)

    return render(request, "entity_form.html", {
        "form": form,
        "title": "Edit Visit Log",
        "next_url": next_url
    })


@login_required(login_url="login")
def delete_visitlog(request, log_id):
    log = get_object_or_404(VisitLog, id=log_id)

    if request.method == "POST":
        next_url = request.POST.get("next") or "visitlog_list"

        log.delete()
        messages.success(request, "Visit log deleted successfully.")

        return redirect(next_url)

    return render(request, "confirm_delete.html", {
        "object": log,
        "title": "Delete Visit Log",
        "cancel_url": "visitlog_list"
    })