from bobtail import (
    Request,
    Response,
)

class Static:

    def get(self, req: Request, res: Response) -> None:
        res.set_static(req.path)
