import pymysql

# สร้างฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล MySQL
def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())
