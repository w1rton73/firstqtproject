import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from vkusnoitochkapay import Ui_coordwidget
import sqlite3
import random


con = sqlite3.connect("food.sqlite")


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vkusno i tochka.ui', self)
        #self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        #self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        #self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        #self.FriesSides.clicked.connect(self.FriesSidesclick)
        #self.HappyMeal.clicked.connect(self.HappyMealclick)
        #self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        #self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        #self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.price = []
        self.call = []
        self.number = []
        self.ids = []
        self.fullprice = 0
        self.fullcall = 0


    def breakfastclick(self):
        uic.loadUi('vkusno i tochkabreakfast.ui', self)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)



    def burgersclick(self):
        uic.loadUi('vkusno i tochkaburgers.ui', self)
        #self.breakfast.clicked.connect(self.breakfastclick)
        #self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        #self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        #self.FriesSides.clicked.connect(self.FriesSidesclick)
        #self.HappyMeal.clicked.connect(self.HappyMealclick)
        #self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        #self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        #self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)
        self.BigMac.clicked.connect(self.bigmacclick)
        self.QuarterPounderWithCheese.clicked.connect(self.QuarterPounderWithCheeseclick)
        self.QuarterPounderWithCheeseDeluxe.clicked.connect(self.QuarterPounderWithCheeseDeluxeclick)
        self.McDouble.clicked.connect(self.McDoubleclick)
        self.QuarterPounderWithCheeseBacon.clicked.connect(self.QuarterPounderWithCheeseBaconclick)
        self.label.setText(f'{self.fullcall}кал')
        self.label_2.setText(f'{self.fullprice}руб')

    def ChickenFishSandwichesclick(self):
        uic.loadUi('vkusno i tochkaChickenFishSandwiches.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

    def McNuggetsAndMealsclick(self):
        uic.loadUi('vkusno i tochkaMcNuggetsAndMeals.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

    def FriesSidesclick(self):
        uic.loadUi('vkusno i tochkaFriesSides.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

    def HappyMealclick(self):
        uic.loadUi('vkusno i tochkaHappyMeal.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

    def McCafeCoffeesclick(self):
        uic.loadUi('vkusno i tochkaMcCafeCoffees.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

    def SweetsTreatsclick(self):
        uic.loadUi('vkusno i tochkaSweetsTreats.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

    def McCafeBakeryclick(self):
        uic.loadUi('vkusno i tochkaMcCafeBakery.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.buy.clicked.connect(self.buyclick)

    def QuarterPounderWithCheeseclick(self):
        uic.loadUi('BaconEggCheeseBiscuit.ui', self)
        with open("BaconEggCheeseBiscuit", encoding='utf8') as f:
            self.textEdit.setText(f.read())
        self.pushButton.clicked.connect(self.burgerssclick)

    def burgerssclick(self):
            value = int(self.spinBox.value())
            pricee = 300
            call = 520
            self.price.append(pricee * value)
            self.call.append(call * value)
            self.fullprice = sum(self.price)
            self.fullcall = sum(self.call)
            self.burgersclick()

    def bigmacclick(self):
        uic.loadUi('bigmac.ui', self)
        with open("bigmac", encoding='utf8') as f:
            self.textEdit.setText(f.read())
        self.pushButton.clicked.connect(self.bigmacc)

    def bigmacc(self):
            value = int(self.spinBox.value())
            pricee = 135
            call = 550
            self.price.append(pricee * value)
            self.call.append(call * value)
            self.fullprice = sum(self.price)
            self.fullcall = sum(self.call)
            self.burgersclick()

    def QuarterPounderWithCheeseDeluxeclick(self):
        uic.loadUi('QuarterPounderWithCheeseDeluxe.ui', self)
        with open("QuarterPounderWithCheeseDeluxe", encoding='utf8') as f:
            self.textEdit.setText(f.read())
        self.pushButton.clicked.connect(self.deluxe)

    def deluxe(self):
            value = int(self.spinBox.value())
            pricee = 360
            call = 630
            self.price.append(pricee * value)
            self.call.append(call * value)
            self.fullprice = sum(self.price)
            self.fullcall = sum(self.call)
            self.burgersclick()

    def McDoubleclick(self):
        uic.loadUi('McDouble.ui', self)
        with open("McDouble", encoding='utf8') as f:
            self.textEdit.setText(f.read())
        self.pushButton.clicked.connect(self.Double)

    def Double(self):
            value = int(self.spinBox.value())
            pricee = 200
            call = 400
            self.price.append(pricee * value)
            self.call.append(call * value)
            self.fullprice = sum(self.price)
            self.fullcall = sum(self.call)
            self.burgersclick()

    def QuarterPounderWithCheeseBaconclick(self):
        uic.loadUi('QuarterPounderWithCheeseBacon.ui', self)
        with open("QuarterPounderWithCheeseBacon", encoding='utf8') as f:
            self.textEdit.setText(f.read())
        self.pushButton.clicked.connect(self.cbac)

    def cbac(self):
            value = int(self.spinBox.value())
            pricee = 330
            call = 630
            self.price.append(pricee * value)
            self.call.append(call * value)
            self.fullprice = sum(self.price)
            self.fullcall = sum(self.call)
            self.burgersclick()

    def buyclick(self):
        if self.fullprice:
            uic.loadUi('vkusno i tochkamainwindow.ui', self)
            check = ""
            check = check + str(random.randrange(10))
            check = check + str(random.randrange(10))
            check = check + str(random.randrange(10))
            check = check + str(random.randrange(10))
            check = check + str(random.randrange(10))
            self.label.setText(f"{check}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())