from bobtail import (
    BobTail,
    AbstractRoute,
    Request,
    Response,
    BaseOptions,
)
from bobtail_cors import BobtailCORS
from bobtail_logger import BobtailLogger
from bobtail_upload import BobtailUpload
from bobtail_jinja2 import BobtailJinja2


class Options(BaseOptions):
    pass


class Home:

    def get(self, req: Request, res: Response):
        res.set_headers({
            "Content-Type": "text/plain",
        })
        data = {
            "title": "Welcome To Joe's Tech Blog",
            "h1": "Welcome To Joe's Tech Blog",
        }
        res.jinja2.render(res, "routes/home.jinja2", data=data)


routes = [
    (Home(), "/"),
]

app = BobTail(Options, routes=routes)

# middleware
app.use(BobtailCORS())
app.use(BobtailLogger())
app.use(BobtailUpload())
app.use(BobtailJinja2(template_dir="templates"))
