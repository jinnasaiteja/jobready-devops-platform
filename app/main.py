from fastapi import FastAPI
from pydantic import BaseModel
import logging
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# enable Prometheus metrics
Instrumentator().instrument(app).expose(app)

# In-memory DB
users = []
class User(BaseModel):
    name: str
    email: str

@app.get("/health")
def health():
    logger.info("Health check endpoint hit")
    return {"status": "ok"}

@app.get("/users")
def get_users():
    logger.info("Fetching users")
    return users

@app.post("/users")
def create_user(user: User):
    logger.info(f"Creating user: {user.name}")
    users.append(user.dict())
    return {"message": "User created", "user": user}
@app.get("/")
def root():
    return {"message": "CI/CD deployment working"}
