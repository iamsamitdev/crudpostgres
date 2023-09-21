import psycopg2

# สร้างฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล PostgreSQL
def connectdb():
    # Localhost
    # connection = psycopg2.connect(
    #     host="localhost",
    #     user="postgres",
    #     password="12345678",
    #     database="sampledb",
    #     port=5432
    # )
    # Server
    connection = psycopg2.connect(
        host="dpg-ck5snn0s0i2c73bv7h20-a",
        user="admin",
        password="iSX0MfPPfZhhlzAfLqxpI9JTxTmxaMMO",
        database="sampledb_3te8",
        port=5432
    )
    return connection


# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())