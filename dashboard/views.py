from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from visitors.models import Visitor, VisitLog


@login_required(login_url="login")
def dashboard(request):
    today = timezone.localdate()

    logs = VisitLog.objects.select_related(
        "visitor",
        "department",
        "user"
    ).order_by("-visit_date", "-check_in_time")

    context = {
        "logs": logs,
        "total_visitors_today": logs.filter(visit_date=today).count(),
        "currently_inside": logs.filter(status__iexact="Inside").count(),
        "total_visitors": Visitor.objects.count(),
    }

    return render(request, "dashboard.html", context)