import pickle
# #对 Mysql文件 进行初始化
path = 'mysql.txt'
# f = open(path,'wb')
# dict = {}
# pickle.dump(dict,f)
#
f = open(path,'rb')
print(pickle.load(f))
