"""
卡类
卡号 密码 余额 卡的状态
"""
class Card:
    def __init__(self,cardId,password,money):
        self.cardId = cardId
        self.password = password
        self.money = money
        self.cardLock = False







