from starlette.responses import HTMLResponse, FileResponse


def main_service():
    return FileResponse('src/static/main.html')