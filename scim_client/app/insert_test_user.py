from app.database import SessionLocal
from app.models import User

def insert_test_user():
    db = SessionLocal()
    try:
        user = User(
            userName="jdoe",
            givenName="John",
            familyName="Doe",
            email="jdoe@example.com",
            active=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        print("✅ Usuario insertado:", user.id, user.userName)
    except Exception as e:
        db.rollback()
        print("❌ Error al insertar usuario:", e)
    finally:
        db.close()

if __name__ == "__main__":
    insert_test_user()
