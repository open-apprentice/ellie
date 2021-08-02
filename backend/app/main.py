import uvicorn

from app import app
from .models.models import User
from .models.schemas.user import User as SchemaUser


@app.post("/user/")
async def create_user(user: SchemaUser):
    user_id = await User.create(**user.dict())
    return {"user_id": user_id}


@app.get("/user/{id}", response_model=SchemaUser)
async def get_user(id: int):
    user = await User.get(id)
    return SchemaUser(**user).dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
