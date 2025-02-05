from fastapi import FastAPI
from datetime import datetime, timezone
from pydantic import BaseModel


app = FastAPI()


class InfoRead(BaseModel):
    email: str
    date: datetime
    github_url: str


@app.get("/", response_model=InfoRead, tags=["Info"], status_code=200)
def get_my_info():
    return InfoRead(
        email="olaidesamson90@gmail.com",
        date=datetime.now(timezone.utc),
        github_url="https://github.com/SOO2023/HNG0",
    )
