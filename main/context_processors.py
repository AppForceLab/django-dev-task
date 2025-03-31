from django.conf import settings


def settings_context(request):
    """
    Inject Django settings into all templates.
    """
    return {
        "DEBUG": settings.DEBUG,
        "LANGUAGE_CODE": settings.LANGUAGE_CODE,
        "TIME_ZONE": settings.TIME_ZONE,
        "USE_TZ": settings.USE_TZ,
    }
