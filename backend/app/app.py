from db import db
from fastapi import FastAPI

# description = """
# We are teachers and so Ellie is neither complicated nor simplistic.
# Ellie is just right so you can focus on teaching and your students.
# Discover Ellie a modern teaching and learning platform.
# """
#
# app = FastAPI(title="Ellie Teaching and Learning Platform", description=description, version="0.0.1",
#               terms_of_service="https://ellieplatform.org/terms-and-conditions/",
#               contact={"name": "Ellie Platform", "url": "https://ellieplatform.org/contact"},
#               license_info={"name": "MIT", "url": "https://github.com/open-apprentice/ellie/blob/main/LICENSE"})

app = FastAPI(title="Ellie")


@app.on_event("startup")
async def startup() -> None:
    await db.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await db.disconnect()
