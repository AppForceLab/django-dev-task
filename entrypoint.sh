#!/bin/sh

# Migrate database
python manage.py migrate

# Create superuser
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists() or \
User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" \
| python manage.py shell

FIXTURE_FILE=main/fixtures/sample_cv.json
if [ -f "$FIXTURE_FILE" ]; then
  echo "Loading fixture: $FIXTURE_FILE"
  python manage.py loaddata "$FIXTURE_FILE"
else
  echo "Fixture not found: $FIXTURE_FILE. Skipping loaddata."
fi


# Start server
exec python manage.py runserver 0.0.0.0:8000
