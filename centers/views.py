from django.shortcuts import render

# Models
from centers.models import Center


def center_list(request):
    centers = Center.objects.all()
    return render(request, "centers/list.html", {
        'centers': centers
    })
