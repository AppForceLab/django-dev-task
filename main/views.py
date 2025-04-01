import tempfile
import os
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from openai import OpenAI
from weasyprint import HTML

from .constants import TRANSLATION_LANGUAGES
from .models import CV
from .tasks import send_pdf_to_email

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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

    return render(
        request,
        "main/cv_detail.html",
        {"cv": cv, "languages": TRANSLATION_LANGUAGES},
    )


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


import json


def translate_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk)

    if request.method == "POST":
        language_code = request.POST.get("language")
        language_name = dict(TRANSLATION_LANGUAGES).get(language_code, "Unknown")

        content = f"""
        Translate each field separately into {language_name} and return in JSON format:

        Bio: {cv.bio}
        Skills: {cv.skills}
        Projects: {cv.projects}
        Contacts: {cv.contacts}

        Return format:
        {{
          "bio": "...",
          "skills": "...",
          "projects": "...",
          "contacts": "..."
        }}
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": content}],
                temperature=0.7,
                response_format={"type": "json_object"},
            )
            translation_json = response.choices[0].message.content.strip()

            translation_dict = json.loads(translation_json)

            return JsonResponse(
                {
                    "status": "success",
                    "translation": translation_json,
                    "language_name": language_name,
                }
            )
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
