from admin import Admin
from Processingfunction import Func
import pickle
def run():
    # 将判断用户登录处理 和显示界面的admin类 实例化
    admin = Admin()
    #调用显示 登录的界面
    admin.welcomeView()
    #判断 如果 为假 也就是 登录失败的情况下  下面的代码 不在执行
    # if not admin.adminLogin():
    #     return
    #调用显示功能界面
    while True:
        admin.showFunc()
        choose = input("请输入 你要 操作的功能")
        atm = Func() #实例化 银行各种操作的类
        if choose == '1':
            atm.createUser()
        elif choose == '2':
            atm.checkBalance()
        elif choose == '3':
            print("你选择了存款的操作")
        elif choose == '4':
            print("你选择了取款的操作")

        #用户的信息(更改或者没有更改的数据信息)
        userData = atm.allUserData
        f = open("mysql.txt","wb")
        pickle.dump(userData,f)
        f.close()

# 208942
run()