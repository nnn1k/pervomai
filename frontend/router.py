from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='frontend/pages/')

router = APIRouter(
    prefix="",
)


@router.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("main/main.html", {"request": request})


@router.get("/info")
def main_page(request: Request):
    return templates.TemplateResponse("info/info.html", {"request": request})


@router.get("/gallery")
def main_page(request: Request):
    return templates.TemplateResponse("gallery/gallery.html", {"request": request})


@router.get("/news")
def main_page(request: Request):
    return templates.TemplateResponse("news/news.html", {"request": request})


@router.get("/admin")
def main_page(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


@router.get("/admin_panel")
def main_page(request: Request):
    return templates.TemplateResponse("admin/panel.html", {"request": request})
