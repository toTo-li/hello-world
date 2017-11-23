import time
class Admin:
    root = 'admin'
    password = '123456'
    def welcomeView(self):
        print('*****************************************************************')
        print('*                                                               *')
        print('*                                                               *')
        print('*                         欢迎登陆刚哥银行                       *')
        print('*                                                               *')
        print('*                                                               *')
        print('*****************************************************************')

    def showFunc(self):
        print('****************************************************************')
        print('*      （1）开户                （2）查余额                     *')
        print('*      （3）存款                （4）取款                       *')
        print('*      （5）转账                （6）解锁                       *')
        print('*      （7）改密码              （8）销户                       *')
        print('*                                                              *')
        print('****************************************************************')
    def adminLogin(self):
        userName = input("请输入管理员账号")
        userPass = input("请输入管理员密码")
        if userName != self.root:
            print("请输入正确的用户名")
            return False
        if userPass != self.password:
            print("请输入正确的密码")
            return False
        print("登录成功 请稍后...")
        time.sleep(3)
        print("欢迎",self.root)
        return True

# myAdmin = Admin()
# myAdmin.printAdeminView()
# myAdmin.adminLogin()