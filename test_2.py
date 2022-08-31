import time
class GetInitialDate(object):
    #  The first date
    #  请更换你的纪念日， 如果数量很多， 可以生成列表，
    #  遍历传值，不懂的可以私聊我
    #  其实这个天数也可以直接从对象中传值过来，但是必须得是 ****-**-** 这样的格式
    Initial_date = "2022-07-15"

    def __init__(self):
        self.date_item = self.get_items
        self.now_date = self._get_now_date()
        # self.Initial_date_sum = self.get_sum_date(self.Initial_date)
        # self.now_date_sum = self.get_sum_date(self.now_date)
        self.all_date = self.get_sum_date(self.Initial_date, self.now_date)

    def __str__(self):
        """稍微修饰一下,"""
        return  f"宝宝今天是我们在一起第{self.all_date} 天呢\n今天也是爱你的一天呢，早安！\n"

    @property
    def get_items(self):
        """遍历或者字典天数
         as:  {1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
         如果是闰年 后续需要加一天"""
        date_items = {}
        s = 0
        for i in range(1, 13):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                s += 31
            elif i == 2:
                s += 28
            else:
                s += 30
            date_items[i] = s
        return date_items

    def get_sum_date(self, old_date, new_date):
        """ start sum the date """
        old_year, old_month, old_d = map(int, old_date.split("-"))
        new_year, new_month, new_d = map(int, new_date.split('-'))
        #  先计算初始日期的天数
        is_leap = True if self._is_leap(old_year) else False
        if not is_leap:
            The_date = self.date_item[old_month] + old_d
        else:
            The_date = self.date_item[old_month] + 1 + old_d
            # 计算新的日期
        is_leap_now = True if self._is_leap(new_year) else False
        if not is_leap:
            The_date_now = self.date_item[new_month] + new_d
        else:
            The_date_now = self.date_item[new_month] + 1 + new_d
        # 比较

        if old_year == new_year:
            return The_date_now - The_date + 2
        else:
            # 2019  2020
            ss = 0
            for i in range(new_year - old_year):
                if self._is_leap(old_year + i):
                    s = 366
                else:
                    s = 365
                ss += s
            return ss + The_date_now - The_date + 2

    def _get_now_date(self):
        """Return the  localtime as: "****-**-**" date """
        return time.strftime("%Y-%m-%d", time.localtime())

    def _is_leap(self, year):
        "year -> 1 if leap year, else 0."
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(GetInitialDate())