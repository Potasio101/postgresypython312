from app.database import engine
from app.models import Base

def init():
    print("⏳ Creando tablas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas con éxito.")

if __name__ == "__main__":
    init()
