import random
from card import Card
from user import User
import time
import pickle
class Func:
    def __init__(self):
        f = open("mysql.txt","rb")
        self.allUserData = pickle.load(f)
        f.close()
    #创建 用户 也就是 开户的功能
    def createUser(self):
        name = input("请输入你的姓名")
        id = input("请输入你的身份证号码")
        phone = input("请输入你的手机号码")
        userMoney = int(input("请输入你的存款金额"))
        if userMoney<=0:
            print("请输入 正确的存款金额")
            return
        userPassword = input("请输入 你的密码")
        #确认密码 输入 3次的功能
        myList = [3,2,1,0]
        for i in myList:
            repass = input("请输入确认密码")
            if userPassword==repass:
                break
            elif i-1!=0:
                print("输入 错误 您还有{}次输入的机会".format(i-1))
            else:
                print("您输入的错误 超过了三次 请回到操作台 再次选择你要选择的操作")
                return
        #生成一个新卡号
        #写一个方法 检测 新生成的卡号 是否存在 存在 则继续生成新的 不存在 则往下继续执行
        cardID = random.randrange(100000,666666)
        newCard = Card(userPassword,cardID,userMoney)
        user = User(name,phone,id,newCard)
        self.allUserData[cardID] = user
        """
        {卡号:user}
        1
        {1:"asda",2:"sdd"}
        """
        print("恭喜你 开户成功 卡号为",cardID)
    #查询 余额
    def checkBalance(self):
        while True:
            cardID = int(input("请输入卡号"))
            cardPassword = input("输入卡密码")
            cardVal = self.allUserData.get(cardID) #通过卡号 来检测这个卡号是否存在
            if cardVal:
                #获取卡的密码
                if cardVal.userCard.cardPass == cardPassword:
                    break
        #可以在这个位置上  加一个 判断该卡 是否锁定 如果锁定了 那么就去 解锁
        print("您的卡的余额为{} .00元".format(cardVal.userCard.cardMoney))
        time.sleep(3)




# myFunc = Func()
# myFunc.createUser()