import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from vkusnoitochkapay import Ui_coordwidget
import sqlite3


con = sqlite3.connect("food.sqlite")


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vkusno i tochka.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.burgers.clicked.connect(self.burgersclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.ids = []

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

        self.BaconEggCheeseBiscuit.clicked.connect(self.BaconEggCheeseBiscuitclick)

    def burgersclick(self):
        uic.loadUi('vkusno i tochkaburgers.ui', self)
        self.breakfast.clicked.connect(self.breakfastclick)
        self.ChickenFishSandwiches.clicked.connect(self.ChickenFishSandwichesclick)
        self.McNuggetsAndMeals.clicked.connect(self.McNuggetsAndMealsclick)
        self.FriesSides.clicked.connect(self.FriesSidesclick)
        self.HappyMeal.clicked.connect(self.HappyMealclick)
        self.McCafeCoffees.clicked.connect(self.McCafeCoffeesclick)
        self.SweetsTreats.clicked.connect(self.SweetsTreatsclick)
        self.McCafeBakery.clicked.connect(self.McCafeBakeryclick)
        self.buy.clicked.connect(self.buyclick)

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

    def BaconEggCheeseBiscuitclick(self):
        uic.loadUi('BaconEggCheeseBiscuit.ui', self)
        with open("BaconEggCheeseBiscuit", encoding='utf8') as f:
            self.textEdit.setText(f.read())

    def buyclick(self):
        uic.loadUi('vkusno i tochkamainwindow.ui', self)
        self.buy.clicked.connect(self.addnewwidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())