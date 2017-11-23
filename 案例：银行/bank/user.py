"""
存储 用户的信息
"""
class User:
    def __init__(self,name,phone,id,userCard):
        self.name = name #用户名
        self.phone = phone #手机号
        self.id = id #身份证号
        self.userCard = userCard #将卡的对象 存储 给 用户的一个属性


