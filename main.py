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
        self.QuarterPounderWithCheese.clicked.connect(self.QuarterPounderWithCheeseclick)
        self.label.setText(f'{self.fullcall}')
        self.label_2.setText(f'{self.fullprice}')

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
            self.value = int(self.spinBox.value())
            print(self.value)
            pricee = 300
            call = 520
            self.price.append(pricee * self.value)
            self.call.append(call * self.value)
            print(call * self.spinBox.value(), pricee * self.spinBox.value())
            self.fullprice = sum(self.price)
            self.fullcall = sum(self.call)
            self.burgersclick()

    def buyclick(self):
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