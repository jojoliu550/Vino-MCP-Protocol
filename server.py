from fastapi import FastAPI
from wine_db import mock_wine_db

app = FastAPI(title="Vino-MCP Server")


@app.get("/")
def root():
    return {
        "name": "Vino-MCP Server",
        "status": "running",
        "wine_count": len(mock_wine_db)
    }


@app.get("/wines")
def get_wines():
    return {"items": mock_wine_db}


@app.get("/wines/search")
def search_wines(q: str = ""):
    q = q.lower().strip()

    if not q:
        return {"items": mock_wine_db}

    results = []
    for wine in mock_wine_db:
        text = " ".join([
            wine.get("name", ""),
            wine.get("cn_name", ""),
            wine.get("region", ""),
            wine.get("grapes", ""),
            wine.get("notes", ""),
            wine.get("pairing", ""),
            " ".join(wine.get("agent_tags", []))
        ]).lower()

        if q in text:
            results.append(wine)

    return {"items": results, "query": q}
