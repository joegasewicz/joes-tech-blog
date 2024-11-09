from bobtail import (
    BobTail,
    Request,
    Response,
    BaseOptions,
)
from bobtail_cors import BobtailCORS
from bobtail_logger import BobtailLogger
from bobtail_upload import BobtailUpload
from bobtail_jinja2 import BobtailJinja2

from api.routes.home import Home
from api.routes.static import Static


class Options(BaseOptions):
    STATIC_DIR = "static"


routes = [
    (Static(), "/static/*"),
    (Home(), "/"),
]


def create_app() -> BobTail:
    app = BobTail(Options, routes=routes)
    # middleware
    app.use(BobtailCORS())
    app.use(BobtailLogger())
    app.use(BobtailUpload())
    app.use(BobtailJinja2(template_dir="api/templates"))
    return app
