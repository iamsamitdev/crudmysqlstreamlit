import streamlit as st
import pymysql
import connectmysql as con

st.title("CRUD MySQL App with Streamlit")

# สร้างออปเจ็กต์เพื่อเชื่อมต่อฐานข้อมูล
connection = con.connectdb()
cursor = connection.cursor()


# สร้างฟังก์ชันสำหรับอ่านข้อมูลจากตาราง person
def read_person():
    cursor.execute("SELECT * FROM person ORDER BY id DESC")
    persons = cursor.fetchall()
    return persons


# สร้างฟังก์ชันสำหรับเพิ่มข้อมูลลงในตาราง person
def create_person(fullname="", email="", age=0):
    try:
        cursor.execute(
            "INSERT INTO person (fullname, email, age) VALUES (%s, %s, %s)", (fullname, email, age)
        )
        connection.commit()
        st.success("บันทึกข้อมูลเรียบร้อยแล้ว")
    except pymysql.Error:
        st.error(f'เกิดข้อผิดพลาด: {pymysql.Error}')


# สร้างฟังก์ชันสำหรับอัปเดตข้อมูลในตาราง person
def update_person(id=0, fullname="", email="", age=0):
    try:
        cursor.execute(
            "UPDATE person SET fullname=%s, email=%s, age=%s WHERE id=%s", (fullname, email, age, id)
        )
        connection.commit()
        st.success('อัพเดทข้อมูลเรียบร้อยแล้ว')
    except pymysql.Error:
        st.error(f'เกิดข้อผิดพลาด: {pymysql.Error}')


# สร้างฟังก์ชันสำหรับลบข้อมูลในตาราง person
def delete_person(id=0):
    try:
        cursor.execute("DELETE FROM person WHERE id=%s", (id))
        connection.commit()
        st.success('ลบข้อมูลเรียบร้อยแล้ว')
    except pymysql.Error:
        st.error(f'เกิดข้อผิดพลาด: {pymysql.Error}')


# สร้างเมนู sidebar
menu = ["Home", "Insert", "Update", "Delete"]

# สร้างตัวเลือกใน sidebar
choice = st.sidebar.selectbox("Menu", menu)

# เมื่อผู้ใช้เลือกเมนู Home
if choice == "Home":
    st.write("### Person List")

    # เรียกใช้งานฟังก์ชัน read_person()
    persons = read_person()

    # วนลูปแสดงข้อมูลจากตาราง person ในฐานข้อมูล
    table_data = []
    if persons:
        for person in persons:
            row = person
            table_data.append(row)
        st.table(table_data)
    else:
        st.write("## ยังไม่มีข้อมูลในตาราง person")


# เมื่อผู้ใช้เลือกเมนู Insert
elif choice == "Insert":
    st.write("### Add new Person")
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 1, 100, 1)

    # button create
    if st.button("Create"):
        if fullname and email and age:
            create_person(fullname, email, age)
        else:
            st.warning("กรุณากรอกข้อมูลให้ครบ")


# เมื่อผู้ใช้เลือกเมนู Update
elif choice == "Update":
    st.write("### Update Person")
    id = st.number_input("ID", 1, 1000, 1)
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", 1, 100, 1)

    # button update
    if st.button("Update"):
        update_person(id, fullname, email, age)


# เมื่อผู้ใช้เลือกเมนู Delete
elif choice == "Delete":
    st.write("### Delete Person")
    id = st.number_input("ID", 1, 1000, 1)

    # button delete
    if st.button("Delete"):
        delete_person(id)