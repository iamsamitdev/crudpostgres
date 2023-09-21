import psycopg2

# สร้างฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล PostgreSQL
def connectdb():
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="12345678",
        database="sampledb",
        port=5432
    )
    return connection


# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())