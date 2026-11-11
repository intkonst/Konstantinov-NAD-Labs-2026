from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.handlers import ros_command_router

app = FastAPI(title="Robolab — команды ROS", docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
app.include_router(ros_command_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000)
