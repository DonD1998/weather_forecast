class ChiShi():
    # chilejijing = 30  # 这个属性是可以被直接修改的，如果不修改就成为类的默认值
    def chi(self):
        chilejijing = 30
        print('吃屎啦')
        return chilejijing

wolade  = ChiShi()

wolade.chi()


# wolade.chilejijing = 10

print(f'到底吃了几斤啊：{wolade.chi()}')

# talade = ChiShi()
#
# talade.chilejijing = 20
# print(talade.chilejijing)
#
# print(f'到底吃了几斤啊：{wolade.chilejijing}')