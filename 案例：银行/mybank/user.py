"""
存储用户信息的类
类的属性
姓名 身份证号
电话
卡
"""
class User:
    def __init__(self,name,idCard,phone,card):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.card = card


