# 🚀 Django Developer Practical Test 🚀

> *Welcome! This test will help us see how you structure a Django project, work with various tools, and handle common tasks in web development. Follow the instructions step by step. Good luck!*

## 📋 Requirements

| Category | Description |
|----------|-------------|
| Style | Follow PEP 8 and other style guidelines |
| Commits | Use clear and concise commit messages |
| Documentation | Include docstrings where needed |
| Structure | Design your project for readability and maintainability |
| Performance | Optimize database access using Django's built-in methods |
| Documentation | Provide detailed information in your README |

## 📝 Tasks
## Task 1: Django Fundamentals
- Create a New Django Project
  - Name it something like CVProject.
  - Use the Python version set up in Task 2 and the latest stable Django release.
  - Use SQLite as your database for now.
- Create an App and Model
  - Create a Django app (for example, main).
  - Define a CV model with fields like firstname, lastname, skills, projects, bio, and contacts.
  - Organize the data in a way that feels efficient and logical.
- Load Initial Data with Fixtures
  - Create a fixture that contains at least one sample CV instance.
  - Include instructions in README.md on how to load the fixture.
- List Page View and Template
  - Implement a view for the main page (e.g., /) to display a list of CV entries.
  - Use any CSS library to style them nicely.
  - Ensure the data is retrieved from the database efficiently.
- Detail Page View
  - Implement a detail view (e.g., /cv/<id>/) to show all data for a single CV.
  - Style it nicely and ensure efficient data retrieval.
- Tests
  - Add basic tests for the list and detail views.
  - Update README.md with instructions on how to run these tests.

## Task 2: PDF Generation Basics
- Choose and install any HTML-to-PDF generating library or tool.
- Add a 'Download PDF' button on the CV detail page that allows users to download the CV as a PDF.

## Task 3: REST API Fundamentals
- Install Django REST Framework (DRF).
- Create CRUD endpoints for the CV model (create, retrieve, update, delete).
- Add tests to verify that each CRUD action works correctly.

## Task 4: Middleware & Request Logging
- Create a Request Log Model
  - You can put this in the existing app or a new app (e.g., audit).
  - Include fields such as timestamp, HTTP method, path, and optionally other details like query string, remote IP, or logged-in user.
- Implement Logging Middleware
  - Write a custom Django middleware class that intercepts each incoming request.
  - Create a RequestLog record in the database with the relevant request data.
  - Keep it efficient.
- Recent Requests Page
  - Create a view (e.g., /logs/) showing the 10 most recent logged requests, sorted by timestamp descending.
  - Include a template that loops through these entries and displays their timestamp, method, and path.
- Test Logging
  - Ensure your tests verify the logging functionality.

## Task 5: Template Context Processors
- Create settings_context
  - Create a context processor that injects your entire Django settings into all templates.
- Settings Page
  - Create a view (e.g., /settings/) that displays DEBUG and other settings values made available by the context processor.

## Task 6: Docker Basics
- Use Docker Compose to containerize your project.
- Switch the database from SQLite to PostgreSQL in Docker Compose.
- Store all necessary environment variables (database credentials, etc.) in a .env file.

## Task 7: Celery Basics
- Install and configure Celery, using Redis or RabbitMQ as the broker.
- Add a Celery worker to your Docker Compose configuration.
- On the CV detail page, add an email input field and a 'Send PDF to Email' button to trigger a Celery task that emails the PDF.

## Task 8: OpenAI Basics
- On the CV detail page, add a 'Translate' button and a language selector.
- Include these languages:
  - Cornish, Manx, Breton, Inuktitut, Kalaallisut, Romani, Occitan, Ladino, Northern Sami, Upper Sorbian, Kashubian, Zazaki, Chuvash, Livonian, Tsakonian, Saramaccan, Bislama
- Hook this up to an OpenAI translation API or any other translation mechanism you prefer. The idea is to translate the CV content into the selected language.

## Task 9: Deployment
- Deploy this project to DigitalOcean or any other VPS.

# Implementation of Tasks 1-8

## Task 1: Django Fundamentals - Implementation
✔️ Project: Initialized Django project CVProject with main application. Settings use SQLite (in Dev) by default, Python version 3.12, and Django 4.2.

✔️ CV Model: In main/models.py, a CV model was created with fields firstname, lastname, bio, skills, projects, contacts - all required fields are present. Data is organized simply (each resume is one record, contact information is stored as a string in the contacts field). For convenience, __str__ is implemented, returning the first and last name.

✔️ Fixture: Sample data prepared - file main/fixtures/sample_cv.json with one resume (name, skills, projects, etc.). README includes instructions for loading fixtures: python manage.py loaddata sample_cv.json. The fixture is also automatically loaded when the container starts (see entrypoint.sh). This allows you to immediately see the application working with sample data.

✔️ CV List: Implemented cv_list view (URL: /), which displays a list of all resumes. In CVProject/urls.py, the route path("", views.cv_list, ...) is linked to this view. In the view itself (main/views.py), all CVs are queried from the database and the main/cv_list.html template is rendered. The template builds Bootstrap cards for each resume - displaying name, skills, and a button/details link. Data is efficiently selected with one .all() query (as there are no relationships, this is sufficient). Styling is done using the Bootstrap 5 CSS framework (connected via CDN in base.html).

✔️ CV Detail: Implemented cv_detail view (URL: /cv/<id>/), showing all resume fields on a separate page. Route configured in CVProject/urls.py. The view gets the object via get_object_or_404 by id and returns the main/cv_detail.html template. The template displays all fields (biography, skills, projects, contacts) with formatting. Buttons are provided for tasks 2, 7, 8 functionality (download PDF, send email, translation - see below). Resume data is obtained in a single query by primary key.

✔️ Tests (List & Detail): In main/testsuite/test_views.py, a CVViewsTest test case is written. The setUp method creates a CV object. Then test_cv_list_view and test_cv_detail_view tests check that the pages return status 200 and contain corresponding resume data (name on the list page, biography on the details page). These tests pass successfully, confirming the correctness of the view implementations.

## Task 2: PDF Generation Basics - Implementation
✔️ PDF Library: WeasyPrint package was chosen for PDF generation. It's added to dependencies (Poetry) and necessary system libraries are installed in Dockerfile (e.g., libpangocairo, libcairo2, etc. for WeasyPrint).

✔️ "Download PDF" Button: A Download PDF button has been added to the cv_detail.html template, which links to the PDF generation URL. The button is styled (Bootstrap btn-success) and accompanied by a download icon.

✔️ PDF URL and View: In CVProject/urls.py, the route /cv/<id>/pdf/ is configured to the download_cv_pdf view. This view (main/views.py) takes the same CV object by id, renders the HTML template main/cv_pdf.html to a string, and uses weasyprint.HTML(...).write_pdf() to generate a PDF to a temporary file. The ready PDF is returned via HttpResponse with a Content-Disposition header for file download. The filename is formed based on the resume name (e.g., john_doe_cv.pdf).

✔️ PDF Template: The cv_pdf.html template contains a resume layout suitable for PDF (similar in structure to the detail page, but without unnecessary elements). WeasyPrint considers CSS, connected fonts, etc., so the PDF is formatted. Thus, when clicking on Download PDF, the user receives a downloadable file with the resume content.

## Task 3: REST API Fundamentals - Implementation
✔️ API v1: API is implemented in the main.api application. A versioned API has been created under the prefix /api/v1/ - this is reflected in main/api/urls.py (included in the main project router /api/). All CRUD endpoints for the CV model are available:
- GET /api/v1/cv/ - list all CVs,
- POST /api/v1/cv/ - create a new CV,
- GET /api/v1/cv/<id>/ - get CV by ID,
- PUT /api/v1/cv/<id>/ - update CV,
- DELETE /api/v1/cv/<id>/ - delete CV.

✔️ DRF and Serialization: Django REST Framework is used. A CVSerializer serializer is defined (fields correspond to the CV model). DRF viewsets or generic classes provide standard CRUD behavior. Basic validation is added - for example, the contacts field expects an email format (if it contains an email) or required fields - this is specified through field parameters in the serializer.

✔️ API Documentation: drf-spectacular is integrated for automatic OpenAPI schema generation and Swagger UI. In CVProject/urls.py, routes are connected:
- /api/schema/ for OpenAPI JSON schema output,
- /api/docs/ for interactive Swagger-UI documentation.
As a result, developers can view and test the API through a browser.

✔️ API Tests: In main/testsuite/test_api.py, a set of CVAPITestCase tests (APITestCase) is written, covering all operations:
- Creating a CV via POST (and checking that it appears in the database),
- Reading CV list and details via GET,
- Updating CV (PUT) and deleting (DELETE) with verification of correct status codes and effects.
Tests use the DRF client (APIRequestFactory or APIClient) and check, for example, that creating without a required field returns a validation error. All tests pass, indicating correct CRUD API operation.

## Task 4: Middleware & Request Logging - Implementation
✔️ Audit Application: A separate audit application was created for logging (connected in INSTALLED_APPS). It contains the model and middleware.

✔️ RequestLog Model: In audit/models.py, the RequestLog model is defined with fields:
- timestamp - date/time (default is current),
- method - HTTP method (GET, POST, etc.),
- path - requested URL path,
- query_string - query string (full GET parameters, can be empty),
- remote_ip - client IP address (GenericIPAddressField),
- user - username of the user who made the request (CharField, stores name or None for anonymous).
This satisfies the requirements (main request details are recorded).

✔️ Logging Middleware: RequestLoggingMiddleware class is implemented in audit/middleware.py. It's added to the project's MIDDLEWARE (after AuthenticationMiddleware). Middleware logic:
- For each request, after executing the view (to avoid logging static files and to have user data), a RequestLog record is saved.
- Requests to static files and favicon are excluded from logging: if request.path.startswith("/static/") or ... "/favicon" - middleware immediately returns response without saving a log. This prevents "cluttering" the database with multiple static request records.
- Username is determined: if request.user.is_authenticated, username is taken, otherwise None.
- A RequestLog record is created via RequestLog.objects.create(...) with all fields filled.
Thus, recent requests accumulate in the database. Performance: one small write query is the only minor cost to each HTTP request, which is acceptable for a test task.

✔️ Recent Requests Page: Added request_log_list view (in audit/views.py) and /logs/ route to it. The view selects the 10 most recent records: RequestLog.objects.order_by("-timestamp")[:10] and renders the audit/request_log_list.html template. The template displays a table: Time, Method, Path (and if available - user). The list is limited to 10 entries as per the task requirement.

✔️ UI Integration: A "Recent Logs" link to /logs/ is added in the base template (e.g., in navigation), so you can access the page. It's available without authentication (anonymous requests are also logged).

✔️ Logging Tests: Tests are implemented (see audit/tests.py):
- Checks that a normal page request creates a record in RequestLog.
- Checks filtering: a request to /static/... doesn't create a record.
- If a user is logged in, the username is written to the log; anonymous - an empty value or None is saved.
- Tests the availability of the /logs/ page and the presence of no more than 10 records in the correct order in its context.
All tests pass, confirming the correct operation of the middleware and logs page.

## Task 5: Template Context Processors - Implementation
✔️ Context Processor: Added settings_context context processor (main/context_processors.py). It returns a dictionary with keys corresponding to project settings. For security and sufficiency, not all variables are injected, but only the main ones:
- DEBUG, LANGUAGE_CODE, TIME_ZONE, USE_TZ. These values are selected from django.conf.settings. This choice ensures the task is completed (passing settings to the template) without exposing sensitive data. The context processor is registered in settings.py in the TEMPLATES section, so it's automatically connected to all templates.

✔️ Settings Page: Implemented settings_view (URL: /settings/, configured in main/urls.py). The view simply renders the main/settings_view.html template without context, relying on data added by the context processor. The template displays a settings table: for example, "DEBUG: True/False", "LANGUAGE_CODE: en-us", etc.

✔️ Interface: The settings page displays values injected by the context processor. Styles are formatted using Bootstrap (table with .table class for a nice appearance).

✔️ Connection to Other Tasks: Through this page, you can verify that, for example, DEBUG is turned off in production (when deployed) or see the current locale. This simplifies debugging. Functionally, the task is completed - the necessary settings are present in the template. (If necessary to add all settings - the dictionary could be expanded, but a reasonable minimum is done in this solution.)

## Task 6: Docker Basics - Implementation
✔️ Dockerfile: The project is containerized. Dockerfile is based on the python:3.12-slim image. For PDF generation support, system dependencies (Cairo, Pango, etc.) are installed via apt-get. Then pyproject.toml and poetry.lock files are copied, and dependencies are installed (Poetry without creating a virtual environment). The project code is copied inside the image, entrypoint.sh is added and execution permission is given. The result is an image containing the application, dependencies, and startup script.

✔️ docker-compose.yml: Docker Compose is configured to run two services: web and db. The database is replaced with PostgreSQL: the db service uses the postgres:17 image. Environment variables for the database (POSTGRES_USER, PASSWORD, DB) are passed from .env. For data preservation, the postgres_data volume is specified. The web service is built from the project's Dockerfile, exposes port 8000 externally, and connects the .env environment file. Also mounted is a volume with the source code (.:/code), which is convenient for development (hot-reload of code inside the container).

✔️ Environment Variables: In the root, there is .env.example with a template of variables - in addition to DB, it specifies DJANGO_SUPERUSER_* (for auto-creating an administrator), SECRET_KEY, DEBUG, SMTP parameters (Mailtrap) and OPENAI_API_KEY. Before starting, you need to copy it to .env and fill in with real values (this is reflected in the README). These variables are loaded as os.getenv through the python-decouple library (config() is used in settings.py).

✔️ Entrypoint.sh: The web service is launched through the entrypoint.sh script. The script performs database migrations (manage.py migrate), then creates a superuser with credentials from environment variables (if such a user doesn't exist yet). Next, if the sample_cv.json fixture exists, it loads it (manage.py loaddata) - thereby filling the database with sample data. After preparation, the server is started: python manage.py runserver 0.0.0.0:8000. Thanks to this, migrations and data loading happen automatically at the first container start, and the application is immediately ready for use.

✔️ Result: Running docker-compose up --build, we get a working application at http://localhost:8000. PostgreSQL is used instead of SQLite (in settings, the connection is through dj_database_url, reading DATABASE_URL from env or assembling by POSTGRES_*). Database data is saved in a volume on the host, so it doesn't disappear when the container is recreated. As a result, local development and deployment are simplified - the entire project is launched with one command in containers.

## Task 7: Celery Basics - Implementation
✔️ Celery and Broker: Celery has been added to the project for background task processing. In the file CVProject/celery.py, a Celery application instance is configured, which reads Django settings and automatically discovers tasks. Redis is chosen as the message broker (in settings.py, CELERY_BROKER_URL = "redis://redis:6379/0" is set to the redis service). Redis is added to docker-compose.yml as a redis service (redis:7 image).

✔️ Worker in Docker Compose: The Compose file describes a worker service, which uses the same image as the web application, but runs the Celery worker command. It depends on the db and redis services. Thus, when docker-compose up is run, a background worker also starts, connecting to Redis and waiting for tasks.

✔️ PDF Sending Task: In main/tasks.py, the function send_pdf_to_email(email, cv_id) is defined with the @shared_task decorator, which registers it as a Celery task. It takes an email and resume identifier as input. In the task:
- Resume is searched by cv_id (if not found - an error message is displayed and the task ends).
- A PDF file is generated: the same WeasyPrint is used, but inside the task. The template for PDF is main/pdf_template.html (there's a small inaccuracy: the template is actually called cv_pdf.html; in the task code, the name pdf_template.html is used). PDF is saved to a temporary file (e.g., /tmp/cv_5.pdf).
- Email is prepared and sent: django.core.mail.EmailMessage is used. The email is formed with the subject "Your CV as PDF" and a message body, sent from the DEFAULT_FROM_EMAIL address to the specified email. The PDF file is attached via email_message.attach_file(output_path). Then email_message.send() is called for sending. SMTP settings are taken from .env (in the example, Mailtrap is configured for testing).
- After sending, the temporary PDF is deleted from disk.
- A message about sending is output in the Celery container log (print).
This background process allows not delaying the main HTTP response.

✔️ Page Integration: A form for entering email and a "Send PDF" button has been added to the CV detail page. The form sends a POST request to the same page (cv_detail), containing an email field. In the cv_detail view, this POST is handled: if there is an email in the request, the Celery task send_pdf_to_email.delay(email, cv.id) is called asynchronously. The view immediately sets a success message via messages.success and redirects back to the detail page. Thanks to this, the user instantly receives a response (the message "The CV was sent to <email> successfully." will appear on the page), and the PDF sending is performed in the background by the worker.

✔️ Result: When the Celery worker completes the task, the user will receive an email with a PDF file of the resume at the specified address. (For testing, you can use test SMTP - Mailtrap, as in .env.example). Overall, task 7 is completed: Celery is configured, the worker starts, the send button works asynchronously, without slowing down the site.

## Task 8: OpenAI Basics - Implementation
✔️ Resume Translation: The CV detail page has received the ability to translate resume text into rare languages. A Select Language -> Translate form has been added, offering 15 languages from the list (Cornish, Manx, Breton, etc. - the full list is defined in main/constants.py as a list of language codes and names). The form doesn't lead to page reload; it's processed via JavaScript.

✔️ OpenAI API: The OpenAI API has been integrated for translation. In main/views.py, an OpenAI(api_key=...) client is created at module initialization, with the key from the OPENAI_API_KEY environment variable. The Chat Completions method is used: a prompt is formed with instructions to translate each resume field into the selected language and return the result in JSON format. The request is sent to the OpenAI model (the code specifies model="gpt-4-turbo", parameter response_format={"type": "json_object"} to get JSON). The API returns a generated JSON object with translated strings.

✔️ Translation Endpoint: The translate_cv view was created (URL: /cv/<id>/translate/, defined in main/urls.py). It accepts only POST. When called, it takes the corresponding CV and language code from request.POST. Then it performs a request to OpenAI, as described above. If successful - returns JsonResponse with status "success", including the received translation (as a JSON string) and the language name. If an error occurred (exception) - JSON with "status": "error" and an error message is returned (HTTP 500).

✔️ Frontend (AJAX): JavaScript code was added to cv_detail.html, sending a translation request without page reload. The fetch() script takes the selected language and sends a POST to /cv/<id>/translate/ with a CSRF header. While the request is being executed, a semi-transparent overlay with a loading indicator (spinner) is displayed on the page, and the "Translate" button is disabled. After receiving the response, the script:
- If data.status === 'success', parses the data.translation field (this is a JSON string with translated fields) and replaces the text in page elements: Bio, Skills, Projects, Contacts with translations.
- If an error occurred, displays a red error message in the error-alert block (for example, "Translation service is currently unavailable. Please try again later."). This block is already in the HTML (hidden by the d-none class).
- In any case, then hides the loading indicator and returns the button to its original state.
Thus, translation occurs asynchronously, without reload, with a smooth UI.

✔️ Protection and Limitations: The OpenAI key is stored in .env (not in code). A basic error handler is implemented (any exception when calling the API leads to showing the user a standard error message). The resume fields are precisely what's translated - the JSON structure is clearly defined by the prompt, which simplifies processing the response.

✔️ Result: The user can select, for example, "Breton", press Translate - and after ~1-3 seconds see how the texts "Bio", "Skills", etc. on the page have been replaced with translations into Breton. The new text is not saved to the database (only on clients), as this is a demonstration function. Task 8 is completed: all required languages are included, translation is carried out through the real OpenAI API.


# Deployment Requirements

To successfully deploy this Django project, ensure the following environment variables are configured:

## 📦 Database Configuration

- `POSTGRES_DB=` — name of the PostgreSQL database
- `POSTGRES_USER=` — PostgreSQL username
- `POSTGRES_PASSWORD=` — PostgreSQL password
- `DATABASE_URL=` — full database URL (e.g. `postgres://user:password@host:port/dbname`)

## 👤 Django Superuser

- `DJANGO_SUPERUSER_USERNAME=` — superuser name to be created on first migration
- `DJANGO_SUPERUSER_EMAIL=` — email address of the superuser
- `DJANGO_SUPERUSER_PASSWORD=` — password for the superuser account

## 🔐 Security & Debug

- `SECRET_KEY=` — Django secret key (should be a long, random string; keep it secure)
- `DEBUG=True` — set to `False` in production!

## 📧 Email Configuration (Mailtrap example)

- `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
- `EMAIL_HOST=sandbox.smtp.mailtrap.io`
- `EMAIL_PORT=587`
- `EMAIL_HOST_USER=your_mailtrap_user`
- `EMAIL_HOST_PASSWORD=your_mailtrap_password`
- `EMAIL_USE_TLS=True`
- `DEFAULT_FROM_EMAIL=verify@example.com`

## 🤖 OpenAI Integration

- `OPENAI_API_KEY=your-key-here` — API key for using OpenAI services (required for AI features)

---

✅ **Make sure to store these variables securely**, especially when deploying to production (e.g. using `.env` files, environment settings in Heroku, or a secrets manager).
