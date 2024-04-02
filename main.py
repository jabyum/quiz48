from fastapi import FastAPI
from api.user_api.userapi import user_router
from database import Base, engine
app = FastAPI(docs_url="/")
Base.metadata.create_all(bind=engine)
app.include_router(user_router)

