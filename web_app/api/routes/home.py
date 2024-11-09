from bobtail import (
    Request,
    Response,
)

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
