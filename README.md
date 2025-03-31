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

### 🔵 Task 1: Django Fundamentals

<details open>
<summary><strong>Expand/Collapse Details</strong></summary>

#### 1. Create a New Django Project
- Name it something like `CVProject`.
- Use the Python version set up in Task 2 and the latest stable Django release.
- Use SQLite as your database for now.

#### 2. Create an App and Model
- Create a Django app (for example, `main`).
- Define a `CV` model with fields like `firstname`, `lastname`, `skills`, `projects`, `bio`, and `contacts`.
- Organize the data in a way that feels efficient and logical.

#### 3. Load Initial Data with Fixtures
- Create a fixture that contains at least one sample CV instance.
- Include instructions in `README.md` on how to load the fixture.

#### 4. List Page View and Template
- Implement a view for the main page (e.g., `/`) to display a list of CV entries.
- Use any CSS library to style them nicely.
- Ensure the data is retrieved from the database efficiently.

#### 5. Detail Page View
- Implement a detail view (e.g., `/cv/<id>/`) to show all data for a single CV.
- Style it nicely and ensure efficient data retrieval.

#### 6. Tests
- Add basic tests for the list and detail views.
- Update `README.md` with instructions on how to run these tests.
</details>

### 🔵 Task 2: PDF Generation Basics

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

1. Choose and install any HTML-to-PDF generating library or tool.
2. Add a 'Download PDF' button on the CV detail page that allows users to download the CV as a PDF.
</details>

### 🔵 Task 3: REST API Fundamentals

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

1. Install Django REST Framework (DRF).
2. Create CRUD endpoints for the CV model (create, retrieve, update, delete).
3. Add tests to verify that each CRUD action works correctly.
</details>

### 🔵 Task 4: Middleware & Request Logging

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

#### 1. Create a Request Log Model
- You can put this in the existing app or a new app (e.g., `audit`).
- Include fields such as `timestamp`, `HTTP method`, `path`, and optionally other details like query string, remote IP, or logged-in user.

#### 2. Implement Logging Middleware
- Write a custom Django middleware class that intercepts each incoming request.
- Create a `RequestLog` record in the database with the relevant request data.
- Keep it efficient.

#### 3. Recent Requests Page
- Create a view (e.g., `/logs/`) showing the 10 most recent logged requests, sorted by timestamp descending.
- Include a template that loops through these entries and displays their timestamp, method, and path.

#### 4. Test Logging
- Ensure your tests verify the logging functionality.
</details>

### 🔵 Task 5: Template Context Processors

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

#### 1. Create settings_context
- Create a context processor that injects your entire Django settings into all templates.

#### 2. Settings Page
- Create a view (e.g., `/settings/`) that displays `DEBUG` and other settings values made available by the context processor.
</details>

### 🔵 Task 6: Docker Basics

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

1. Use Docker Compose to containerize your project.
2. Switch the database from SQLite to PostgreSQL in Docker Compose.
3. Store all necessary environment variables (database credentials, etc.) in a `.env` file.
</details>

### 🔵 Task 7: Celery Basics

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

1. Install and configure Celery, using Redis or RabbitMQ as the broker.
2. Add a Celery worker to your Docker Compose configuration.
3. On the CV detail page, add an email input field and a 'Send PDF to Email' button to trigger a Celery task that emails the PDF.
</details>

### 🔵 Task 8: OpenAI Basics

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

1. On the CV detail page, add a 'Translate' button and a language selector.
2. Include these languages:
   - Cornish
   - Manx
   - Breton
   - Inuktitut
   - Kalaallisut
   - Romani
   - Occitan
   - Ladino
   - Northern Sami
   - Upper Sorbian
   - Kashubian
   - Zazaki
   - Chuvash
   - Livonian
   - Tsakonian
   - Saramaccan
   - Bislama
3. Hook this up to an OpenAI translation API or any other translation mechanism you prefer. The idea is to translate the CV content into the selected language.
</details>

### 🔵 Task 9: Deployment

<details>
<summary><strong>Expand/Collapse Details</strong></summary>

Deploy this project to DigitalOcean or any other VPS. 
</details>

---

## 🎉 That's it!

---


## 🛠 Usage Instructions

### 🔐 Environment Variables

Create a `.env` file in the project root based on `.env.example`:

```bash
cp .env.example .env
```

### 📦 Load Sample Data (Fixtures)

To load the initial sample CV data, run the following command:
To run the basic tests for the list and detail views:
```bash
python manage.py loaddata sample_cv.json
```
To run the basic tests for the list and detail views:
```bash
python manage.py test main
```
If everything is set up correctly, you should see output like this:
```bash
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.012s

OK
```
