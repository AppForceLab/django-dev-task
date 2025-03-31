import os
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from weasyprint import HTML
from main.models import CV
from celery import shared_task


@shared_task
def send_pdf_to_email(email, cv_id):
    try:
        cv = CV.objects.get(pk=cv_id)
    except CV.DoesNotExist:
        print(f"CV with id {cv_id} does not exist.")
        return

    # Render HTML content using the existing template
    html_content = render_to_string("main/pdf_template.html", {"cv": cv})

    # Generate a temporary PDF file
    output_path = f"/tmp/cv_{cv_id}.pdf"
    HTML(string=html_content).write_pdf(output_path)

    # Prepare and send the email with the PDF attached
    subject = "Your CV as PDF"
    body = "Please find attached the requested CV PDF."
    from_email = settings.DEFAULT_FROM_EMAIL

    email_message = EmailMessage(subject, body, from_email, [email])
    email_message.attach_file(output_path)
    email_message.send()

    # Clean up the temporary PDF file
    os.remove(output_path)
    print(f"CV PDF sent to {email}")
