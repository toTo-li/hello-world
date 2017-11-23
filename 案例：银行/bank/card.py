#卡类
# 卡密码  卡号 卡余额
class Card:
    def __init__(self,cardPass,cardID,cardMoney):
        self.cardPass = cardPass #卡密码
        self.cardID = cardID #卡号
        self.cardMoney = cardMoney #卡钱
        self.cardLock = False #是否锁卡