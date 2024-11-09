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
from api.database import init_db
from api.models._base import Base


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
    # database
    from api.models.articles import Article
    Base.metadata.create_all(init_db())
    return app
