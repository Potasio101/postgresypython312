import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    print("✅ Conexión exitosa:", cur.fetchone())
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Error al conectar a la base de datos:", e)
