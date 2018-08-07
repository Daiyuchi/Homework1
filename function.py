import db_connect

database=db_connect.database
cursor=db_connect.cursor
db=db_connect.db

#處理information的funtion
class inform:
    @staticmethod
    def add():
        name = input("請輸入你要新增的姓名：")
        cursor.execute("SELECT NAME FROM INFORMATION WHERE NAME = ('%s')" % name)
        result = cursor.fetchall()
        if not result:
            phone = (input("請輸入電話號碼："))
            birth = (input("請輸入生日（格式：00/00/00）:"))
            db = database()
            db.addDB(name, phone, birth)
        else:
            print("已存在。")
    @staticmethod
    def delete():
        name = input("請輸入你要刪除的姓名：")
        cursor.execute("SELECT NAME FROM INFORMATION WHERE NAME = ('%s')" % name)
        result = cursor.fetchall()
        if not result:
            print("無此資料...")
        else:
            db = database()
            db.delete(name)
            print("已刪除'%s'"%name)

    @staticmethod
    def update():
        name = input("請輸入你要更新的姓名：")
        cursor.execute("SELECT NAME FROM INFORMATION WHERE NAME = ('%s')" % name)
        result = cursor.fetchall()
        if not result:
            print("無此資料...")
        else:
            db = database()

            choose = int(input('''要更改什麼資料呢？
            1.電話
            2.生日
            3.都要
                        '''))
            if choose == 1:
                phone = (input("請輸入電話號碼："))
                db.updatePHONE(phone,name)

            elif choose == 2:
                birth = (input("請輸入生日（格式：00/00/00）:"))
                db.updateBIRTH(birth,name)
            elif choose == 3:
                phone = (input("請輸入電話號碼："))
                birth = (input("請輸入生日（格式：00/00/00）:"))
                db.updateALL(phone,birth,name)
            else:
                print('ERROR...')

    @staticmethod
    def display():
        db = database()
        db.display()
#################################################
#功能選擇
def menu():
    print('''
    請選擇你想要的功能：
    1.新增資料
    2.更新資料
    3.刪除資料
    4.顯示所有資料
    5.離開...
    ''')
################################################
#main
while True:
    try:
        menu()
        choose = int(input())
        person = inform()
        if choose ==1:
            person.add()
        elif choose ==2:
            person.update()
        elif choose ==3:
            person.delete()
        elif choose ==4:
            person.display()
        elif choose ==5:
            print("＊＊＊＊程式結束＊＊＊＊")
            break
        else:
            print("ERROR...")
    except:
        print("請輸入對應的數字...")
