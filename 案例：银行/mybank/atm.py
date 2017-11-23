from user import User
from card import Card
import pickle
import random
import time
class ATM:
    def __init__(self):#将所有的用户信息 读取出来
        self.path = 'mysql.txt'
        f = open(self.path, 'rb')
        self.allUsers = pickle.load(f)
        f.close()
    def createUser(self):
        name = input("请输入你的名字")
        idCard = input("请输入身份证号")
        phone = input("请输入你的手机号码")
        userMoney = int(input("请输入你的存款金额"))
        #判断金额
        if userMoney<0:
            print("您的智商余额不足 开卡失败")
            return False
        userPassword = input("请输入你的密码")
        for i in range(1,4): #判断确认密码 次数最多为3次
            num = 1
            password = input("输入确认密码{} 剩余输入次数{}".format(i,3-i))
            if password == userPassword:
                num = 2
                break
        if num==1:
            print('密码输入 错误 开户失败')
            return
        #判断 卡号是否为 新卡号
        while True:
            cardId = random.randrange(10000, 99999)
            if not self.allUsers.get(cardId):
                break
        card = Card(cardId,userPassword,userMoney) #实例化卡的类
        user = User(name,idCard,phone,card) #实例化 用户类
        self.allUsers[cardId] = user #将新的卡的号 和用户对象 写入打 当前所有用户信息的字典里 也就是新添加一个键值对 键为唯一不重复的卡号
        print("恭喜你开户成功 卡号为{}".format(cardId))

    def searchMoney(self):
        #判断卡号是否存在  如果超过三次 下面的代码将不再执行
        for i in range(3):
            cardId = int(input("请输入你要查询余额的卡号"))
            if self.allUsers.get(cardId):
                break
            else:
                if i==2:
                    print("您输入的卡号错误超过三次 请重新选择你要的操作")
                    return False
                print('请输入正确的卡号')
        currentCard = self.allUsers[cardId] #获取当前操作的卡的对象
        #判断卡是否被锁定
        if currentCard.card.cardLock:
            print("该卡已被锁定了 请去解锁")
            return False
        #判断卡的密码
        for i in range(3):
            cardPassword = input("请输入卡的密码")
            if cardPassword == currentCard.card.password:
                break
            else:
                if i == 2:
                    print("您输入的卡的密码错误超过三次 该卡已经被锁定")
                    currentCard.card.cardLock = True
                    return False
                print('请输入正确的密码')
        print("你好{} 您的账户余额为{}元".format(currentCard.name,currentCard.card.money))
        time.sleep(2)

    #转账的方法
    def transferAccounts(self):
        #获取要转账的对方的卡号
        for i in range(3):
            dfCard = int(input("请输入你要转账的卡号"))
            if self.allUsers.get(dfCard):
                break
            else:
                if i==2:
                    print("您输入的卡号错误超过三次 请重新选择你要的操作")
                    return False
                print('请输入正确的卡号')
        #获取当前要转账这个人的卡的余额
        myCardId = input("请输入自己的卡号")


        # money = int(input("请输入您要转账的金额"))

        # if money>