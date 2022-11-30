import gettext
from app.settings import settings
from fastapi.requests import Request

DEFAULT_LANGUAGE = "en"
SUPPORTED_LANGUAGE = ["de", "en", "ru"]


def language_translator(request: Request):
    language = request.headers.get("accept-language", DEFAULT_LANGUAGE)
    if language not in SUPPORTED_LANGUAGE:
        language = DEFAULT_LANGUAGE
    translate = gettext.translation(
        settings.localization_domain,
        localedir=settings.localization_dir,
        languages=[language],
    )
    return translate.gettext
