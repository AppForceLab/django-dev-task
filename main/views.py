from django.shortcuts import render, get_object_or_404
from .models import CV

def cv_list(request):
    cvs = CV.objects.all()
    return render(request, "main/cv_list.html", {"cvs": cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, "main/cv_detail.html", {"cv": cv})