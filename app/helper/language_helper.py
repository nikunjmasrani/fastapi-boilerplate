import gettext
from app.settings import settings
from fastapi.requests import Request

DEFAULT_LANGUAGE = "en"
SUPPORTED_LANGUAGE = ["de", "en", "ru"]


def language_translator(request: Request):
    language = request.headers.get("accept-language", None)
    translate = gettext.translation(
        settings.localization_domain,
        localedir=settings.localization_dir,
        languages=[language],
    )
    return translate.gettext
