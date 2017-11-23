from admin import Admin
from atm import ATM
import pickle
import time
def run():
    admin = Admin()
    #显示 欢迎的界面
    admin.printAdminView()
    #判断登陆成功失败
    # if not admin.adminLogin():
    #     time.sleep(2)
    #     print("登陆失败 请输入正确的登录名和密码")
    #     return
    #显示 功能界面
    # time.sleep(2) #延迟2秒执行
    atm = ATM()
    while True:
        admin.printFunctionView()
        userCommand = input("请选择你的处理业务")
        if userCommand=='1':
            atm.createUser()
        elif userCommand=='2':
            atm.searchMoney()
        elif userCommand=='3':
            print(userCommand)
        elif userCommand=='4':
            print(userCommand)
        elif userCommand=='5':
            print(userCommand)
        elif userCommand=='6':
            print(userCommand)
        elif userCommand=='7':
            print(userCommand)
        elif userCommand=='8':
            print(userCommand)
        elif userCommand=='9':
            allUsers = atm.allUsers
            f = open(atm.path,'wb')
            pickle.dump(allUsers,f)
            f.close()
            break
run()