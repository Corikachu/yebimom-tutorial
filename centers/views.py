from django.shortcuts import render, redirect, get_object_or_404

# Models
from centers.models import Center

# Forms
from centers.forms import CenterForm


def centers_list(request):
    centers = Center.objects.all()
    return render(request, "centers/list.html", {
        'centers': centers
    })


def center_create(request):
    form = CenterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("centers_list")
    return render(request, "centers/form.html", {
        'form': form
    })


def center_update(request, pk):
    center = get_object_or_404(Center, pk=pk)
    form = CenterForm(request.POST or None, instance=center)

    if form.is_valid():
        form.save()
        return redirect("centers_list")
    return render(request, "centers/form.html", {
        'form': form
    })
