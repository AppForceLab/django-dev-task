import tempfile

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from weasyprint import HTML

from .models import CV
from .tasks import send_pdf_to_email


def cv_list(request):
    cvs = CV.objects.all()
    return render(request, "main/cv_list.html", {"cvs": cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)

    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            send_pdf_to_email.delay(email, cv.id)
            messages.success(request, f"The CV was sent to {email} successfully.")
            return redirect("cv_detail", pk=pk)

    return render(request, "main/cv_detail.html", {"cv": cv})


def download_cv_pdf(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    html_string = render_to_string("main/cv_pdf.html", {"cv": cv})

    response = HttpResponse(content_type="application/pdf")
    filename = f"{cv.firstname.lower()}_{cv.lastname.lower()}_cv.pdf"
    response["Content-Disposition"] = f"attachment; filename={filename}"

    with tempfile.NamedTemporaryFile(delete=True) as output:
        HTML(string=html_string).write_pdf(target=output.name)
        output.seek(0)
        response.write(output.read())

    return response


def settings_view(request):
    """Display current Django settings passed via context processor."""
    return render(request, "main/settings_view.html")
