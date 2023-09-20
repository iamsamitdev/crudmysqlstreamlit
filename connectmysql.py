import pymysql

# สร้างฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล MySQL
def connectdb():
    # local
    # connection = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='1234',
    #     db='pythondb',
    #     port=3306,
    #     cursorclass=pymysql.cursors.DictCursor
    # )

    # server
    connection = pymysql.connect(
        host='b3palitjkq6y142h9y0v-mysql.services.clever-cloud.com',
        user='uh7ciudmmxi9gdnp',
        password='L09BGgFWKOzvl9ktggQZ',
        db='b3palitjkq6y142h9y0v',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# ทดสอบเรียกใช้งานฟังก์ชัน
# print(connectdb())
