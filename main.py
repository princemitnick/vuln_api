from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse


app = FastAPI()


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    query = request.query_params.get("q", "")
    return f"<html><body>Resultat pour : <b>{query}</b></body></html>"