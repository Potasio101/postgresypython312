from fastapi import FastAPI, Request, HTTPException, Header
from app.database import SessionLocal
from app.models import User
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Token que Azure enviará (puede venir de env en producción)
EXPECTED_TOKEN = "Bearer supersecreto"

# SCIM-like schema (simplificado)
class Name(BaseModel):
    givenName: Optional[str]
    familyName: Optional[str]

class Email(BaseModel):
    value: str

class SCIMUser(BaseModel):
    userName: str
    name: Optional[Name]
    emails: Optional[list[Email]]
    active: Optional[bool] = True

@app.post("/Users")
async def create_user(scim_user: SCIMUser, authorization: Optional[str] = Header(None)):
    if authorization != EXPECTED_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = SessionLocal()
    try:
        email_value = scim_user.emails[0].value if scim_user.emails else None

        user = User(
            userName=scim_user.userName,
            givenName=scim_user.name.givenName if scim_user.name else None,
            familyName=scim_user.name.familyName if scim_user.name else None,
            email=email_value,
            active=scim_user.active
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"id": user.id, "userName": user.userName}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
