class FriedChicken:

    def __init__(self, flavor, size, price, skin, sauce):
        self.flavor = flavor  # 炸雞的口味
        self.size = size  # 炸雞的尺寸大小
        self.price = price  # 炸雞的價格
        self.skin = skin  # 炸雞的外皮
        self.sauce = sauce  # 炸雞的醬汁

    def display_info(self): #顯示炸雞資訊
        print(f"炸雞口味: {self.flavor}")
        print(f"炸雞尺寸: {self.size}")
        print(f"炸雞價格: {self.price} 元")
        print(f"炸雞外皮麵衣: {self.skin}")
        print(f"炸雞醬汁: {self.sauce}")

    def increase_price(self, amount): #調整價格
        self.price += amount
        print(f"原味價格調整上漲 {amount} 元")

    def change_flavor(self, new_flavor): #變更炸雞口味
        self.flavor = new_flavor
        print(f"韓式炸雞口味變更為 {new_flavor}")

    def adjust_skin(self, new_skin):  #調整炸雞外皮麵衣
        self.skin = new_skin
        print(f"炸雞外皮麵衣為 {new_skin}")

    def portion_size(self, new_size): #調整份量
        self.size = new_size
        print(f"份量大小改為 {new_size}")


if __name__ == "__main__":

    # 創建四個炸雞物件
    ck1 = FriedChicken(flavor="原味", size="大份", price=100, skin="日式", sauce="蜂蜜芥末")
    ck2 = FriedChicken(flavor="香辣", size="中份", price=120, skin="韓式", sauce="辣味")
    ck3 = FriedChicken(flavor="甜辣", size="中份", price=130, skin="泰式", sauce="酸辣")
    ck4 = FriedChicken(flavor="椒鹽", size="大份", price=110, skin="台式", sauce="蜜汁")

    # 分別呼叫副函式
    ck1.increase_price(20)  #調整價格
    ck2.change_flavor("甜辣") #調整口味
    ck3.portion_size("大份") #調整份量大小
    ck4.adjust_skin("日式") #調整炸雞外皮

    # 顯示更新菜單後的炸雞資訊
    ck1.display_info()
    ck2.display_info()
    ck3.display_info()
    ck4.display_info()
