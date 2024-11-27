# worklog/views.py
from django.shortcuts import render, redirect
from .models import WorkLog
from .forms import WorkLogForm

def worklog_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    worklogs = WorkLog.objects.filter(user=request.user)
    return render(request, 'worklog/list.html', {'worklogs': worklogs})
