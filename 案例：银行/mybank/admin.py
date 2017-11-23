class Admin:
    root = 'admin'
    password = '123456'
    '''
    欢迎的界面
    '''
    def printAdminView(self):
        print('(*************************************************)')
        print('(*                   欢迎 dear honey             *)')
        print('(*                   欢迎 dear honey             *)')
        print('(*                   欢迎 dear honey             *)')
        print('(*                   欢迎 dear honey             *)')
        print('(*                   欢迎 dear honey             *)')
        print('(*                   欢迎 dear honey             *)')
        print('(*************************************************)')
    """
    显示功能的界面
    """
    def printFunctionView(self):
        print('(*************************************************)')
        print('(*                    接客开始了                  *)')
        print('(*(1)开户                  (2)查询                *)')
        print('(*(3)取款                  (4)存款                *)')
        print('(*(5)挂失                  (6)解锁                *)')
        print('(*(7)改密                  (8)注销                *)')
        print('(*(10)转账                                         *)')
        print('(*                (9)quit 退出                    *)')
        print('(*************************************************)')
    '''
    判断登陆是否成功
    '''
    def adminLogin(self):
        userroot = input("请输入后台登陆名")
        if userroot!=self.root:
            return False
        userPassword = input('请输入登陆密码')
        if userPassword != self.password:
            return False
        print("登陆成功...")
        return True