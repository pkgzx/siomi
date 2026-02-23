"""This file contains the main application entry point."""

from fastapi import (
    FastAPI,
    Request,
    status
)

import uvicorn


app = FastAPI(
    title="Siomi AI",
    version="0.0.1",
    description="""Siomi is a platform multi-agent AI to generate answers to our clients by messages, documents, graphics, report from big data and more""",
)

@app.get("/")
async def root(request: Request) -> str:
    """Root probe to test api"""
    return "Hello"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)