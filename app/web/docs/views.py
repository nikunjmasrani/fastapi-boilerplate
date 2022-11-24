from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

router = InferringRouter()


@cbv(router)
class Docs:
    @router.get("/docs", include_in_schema=False)
    async def swagger_ui_html(self, request: Request):
        """
        Swagger UI.

        :param request: current request.
        :return: rendered swagger UI.
        """
        title = request.app.title
        return get_swagger_ui_html(
            openapi_url=request.app.openapi_url,
            title=f"{title} - Swagger UI",
            oauth2_redirect_url=request.url_for("swagger_ui_redirect"),
            swagger_js_url="/static/docs/swagger-ui-bundle.js",
            swagger_css_url="/static/docs/swagger-ui.css",
        )

    @router.get("/swagger-redirect", include_in_schema=False)
    async def swagger_ui_redirect(self) :
        """
        Redirect to swagger.

        :return: redirect.
        """
        return get_swagger_ui_oauth2_redirect_html()

    @router.get("/redoc", include_in_schema=False)
    async def redoc_html(self, request: Request) :
        """
        Redoc UI.

        :param request: current request.
        :return: rendered redoc UI.
        """
        title = request.app.title
        return get_redoc_html(
            openapi_url=request.app.openapi_url,
            title=f"{title} - ReDoc",
            redoc_js_url="/static/docs/redoc.standalone.js",
        )
