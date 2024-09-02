import pandas as pd
from tabulate import tabulate
import numpy as np
pd.options.mode.chained_assignment = None 

class ShopItems:
    
    def __init__(self,data) -> None:
        self.data=data
        
        self.category=self.data['Category']
        self.item_code=self.data['item code']
        self.description=self.data['Description']
        self.price=self.data['Price ($)']
        self.items=[]

    def get_items(self,category):
        self.items=[]
        for item in range(len(self.data[self.data['Category'] == category])):
            self.items.append(self.data[self.data['Category'] == category].values[item])
        print(tabulate(self.items, headers=['Category item','Item Code', 'Description','Price $']))
        print("\n")

        return self.items



class Phone(ShopItems):
    def __init__(self):
        super().__init__(data)
        
    def get_phones(self):
        self.phones=[]
        self.phones=self.get_items('Phone')
        return self.phones


class Tablet(ShopItems):
    def __init__(self):
        super().__init__(data)
    
    def get_tablets(self):
        self.tablets=[]
        self.tablets=self.get_items('Tablet')
        return self.tablets

class SimCard(ShopItems):
    def __init__(self):
        super().__init__(data)
    
    def get_sim_cards(self):
        self.sim_cards=[]
        self.sim_cards=self.get_items('SIM card')
        return self.sim_cards

class Case(ShopItems):
    def __init__(self):
        super().__init__(data)
    
    def get_cases(self):
        self.cases=[]
        self.cases=self.get_items('Case')
        return self.cases

class Charger(ShopItems):
    def __init__(self):
        super().__init__(data)
    
    def get_chargers(self):
        self.chargers=[]
        self.chargers=self.get_items('Charger')
        return self.chargers

class GetItem(ShopItems):
    def __init__(self):
        super().__init__(data)
        self.items=ShopItems(data)
        self.phone=Phone()
        self.tablet=Tablet()
        self.sim_card=SimCard()
        self.user_shopping_car=pd.DataFrame()
        self.case=Case()
        self.charger=Charger()


    def get_item(self):
        val=False
        user_device_choose = pd.DataFrame()

        while not val:

            item_code=str(input("Choose your Item by Code Please: ")).upper()
            print("\n")
           
            for item in self.items.item_code:
                if item==item_code:
                    val=True
            if val:
                user_device_choose = self.data[(self.data["item code"] == item_code) ]
                user_device_choose.set_index('item code', inplace=True)

                self.user_shopping_car=self.user_shopping_car._append(user_device_choose)
                
                item_car_shopping_price=self.user_shopping_car['Price ($)'].astype(float)
                
                price_last_item_added=self.user_shopping_car.iat[-1, 2]
                item_code_last_item_added=self.user_shopping_car.iat[-1, 1]
                price_last_item_added=float(price_last_item_added)

                for index, row in self.user_shopping_car.iterrows() :
                    category_frequency=self.user_shopping_car['Category'].count()

                    if row['Category']=="Phone" or row['Category']=="Tablet":

                        if category_frequency>=2 and item_code_last_item_added:

                            discount=price_last_item_added* 0.10
                            final_price=price_last_item_added-discount
                            final_price=round(final_price,2)
                            self.user_shopping_car['Price ($)'].iloc[-1]=final_price


                            print("Applied discount 10% off","\n")
                                                            
                            print("Price Before discount = ",price_last_item_added,"$","\n")

                            print("Price After discount = ",self.user_shopping_car['Price ($)'].iloc[-1],"$","\n")

                            print("Money saved =",round(discount,2),"$","\n")

                            print("ITEM CHOOSEN:","\n")

                            print(tabulate(self.user_shopping_car, headers=['Item Code','Category item', 'Description','Price $']))
                            print("\n")

                            self.get_sim_card()
                            return self.user_shopping_car
                        else:
                            print("ITEM CHOOSEN:","\n")

                            print(tabulate(self.user_shopping_car, headers=['Item Code','Category item', 'Description','Price $']))
                            print("\n")
                            
                            print("Total=",round(item_car_shopping_price.sum(),2))
                            print("\n")
                            
                            self.get_sim_card()
                            return self.user_shopping_car

            else:
                print(" Check the Item Codes above and choose a correct Item Code Please:","\n")
                self.get_item()

            
    def get_sim_card(self):

        val=False
        user_sim_choose = pd.DataFrame()

        while not val:
            self.sim_card.get_sim_cards()
            item_code=str(input("Choose your Sim Card by Code Please: ")).upper()
            print("\n")

            for item in self.items.item_code:
                if item==item_code:
                    val=True
            if val:
                user_sim_choose = self.data[(self.data["item code"] == item_code) ]
                user_sim_choose.set_index('item code', inplace=True)
                self.user_shopping_car=self.user_shopping_car._append(user_sim_choose)
                
                print("ITEM CHOOSEN:","\n")
                print(tabulate(user_sim_choose, headers=['Category item','Item Code', 'Description','Price $']))
                print("\n")
                
                total=self.user_shopping_car['Price ($)'].astype(float)
                print("Total=",round(total.sum(),2))
                print("\n")
                
                self.get_case()
                return user_sim_choose
                
            else:
                print("Check the Item Codes above and choose a correct Item Code Please:","\n")
                self.get_sim_card()
              
    def get_case(self):

        val=False
        user_case_choose = pd.DataFrame()

        while not val:
            self.case.get_cases()
            item_code=str(input("Choose your Case by Code Please: ")).upper()
            print("\n")

            for item in self.items.item_code:
                if item==item_code:
                    val=True
            if val:
                user_case_choose = self.data[(self.data["item code"] == item_code) ]
                user_case_choose.set_index('item code', inplace=True)
                self.user_shopping_car=self.user_shopping_car._append(user_case_choose)
                
                print("ITEM CHOOSEN:","\n")
                print(tabulate(user_case_choose, headers=['Category item','Item Code', 'Description','Price $']))
                print("\n")
                
                total=self.user_shopping_car['Price ($)'].astype(float)
                print("Total=",round(total.sum(),2))
                
                print("\n")
                self.get_charger()
                return user_case_choose
                
                
            else:
                print("Check the Item Codes above and choose a correct Item Code Please:","\n")
                self.get_case()
           
    def get_charger(self):

        val=False

        while not val:
            print("Choose your chargers by number Please")
            print("\n")
            print("1. Car")
            print("2. Home")
            print("3. Both")
            print("4. None")
            print("\n")

            try:
                charger_user=int(str(input("Choose a number from above Please: ")))
                print("\n")
            except ValueError:
                charger_user=int(input("Write the number of your selection Please: "))
            
            match charger_user:
                case 1 :
                    
                    user_charger_choose_car = self.data[(self.data["Description"] == "Car") ]
                    user_charger_choose_car.set_index('item code', inplace=True)
                    self.user_shopping_car=self.user_shopping_car._append(user_charger_choose_car)
                    
                    print("ITEM CHOOSEN:","\n")
                    print(tabulate(user_charger_choose_car, headers=['Category item','Item Code', 'Description','Price $']))
                    print("\n")
                    
                    total=self.user_shopping_car['Price ($)'].astype(float)
                    print("Total=",round(total.sum(),2))
                    print("\n")
                    
                    self.user_car_shopping_summary()
                    return user_charger_choose_car
                
                case 2 :
                    
                    user_charger_choose_home = self.data[(self.data["Description"] == "Home") ]
                    user_charger_choose_home.set_index('item code', inplace=True)
                    self.user_shopping_car=self.user_shopping_car._append(user_charger_choose_home)
                    
                    print("ITEM CHOOSEN:","\n")
                    print(tabulate(user_charger_choose_home, headers=['Category item','Item Code', 'Description','Price $']))
                    print("\n")
                    
                    total=self.user_shopping_car['Price ($)'].astype(float)
                    print("Total=",round(total.sum(),2))
                    print("\n")
                    
                    self.user_car_shopping_summary()
                    return user_charger_choose_home
                
                case 3:

                    user_charger_choose_home = self.data[(self.data["Description"] == "Home") ]
                    user_charger_choose_home.set_index('item code', inplace=True)

                    user_charger_choose_car = self.data[(self.data["Description"] == "Car") ]
                    user_charger_choose_car.set_index('item code', inplace=True)
                    
                    self.user_shopping_car=self.user_shopping_car._append(user_charger_choose_home)
                    self.user_shopping_car=self.user_shopping_car._append(user_charger_choose_car)

                    total=self.user_shopping_car['Price ($)'].astype(float)

                    print("\n")
                    
                    print("Total=",round(total.sum(),2))
                    
                    print("\n")
                    
                    self.user_car_shopping_summary()
                    return  self.user_shopping_car

                case 4 :
                    print("No charger added")
                    print("\n")
                    
                    total=self.user_shopping_car['Price ($)'].astype(float)
                    print("Total=",round(total.sum(),2))
                    
                    print("\n")
                    return self.user_car_shopping_summary()
                    

    def user_selection_device(self):
        
        print("¿What would you like to buy?")
        print("\n")
        print("1. Phone")
        print("2. Tablet")
        print("\n")
        try:
            self.value_device=int(str(input("Choose your device by number Please: ")))
            print("\n")
        except ValueError:
            self.value_device=int(input("Write the number of your selection Please: "))
            print("\n")
        match self.value_device:
            case 1 :
                self.phone.get_phones()
            case 2:
                self.tablet.get_tablets()
        if self.value_device==1 or self.value_device==2:
            return self.get_item()
        else:
            self.user_selection_device()
            
    
    
    def user_car_shopping_summary(self):
        
        print("\n")

        print("This is your summary:")
        print("\n")

        print(self.user_shopping_car)
        print("\n")

        total=self.user_shopping_car['Price ($)'].astype(float)
        print("Total=",round(total.sum(),2),"$")
        
        print("\n")
        print("¿Any additional device?")
        print("\n")

        print("1. Phone")
        print("2. Tablet")
        print("3. No more for now")

        print("\n")
        
        try:
            self.value_device=int(str(input("Choose your device: ")))
            print("\n")
        except ValueError:
            self.value_device=int(input("Write the number of your selection Please: "))
            print("\n")
        match self.value_device:
            case 1 :
                self.phone.get_phones()
                print("\n")
            case 2:
                self.tablet.get_tablets()
                print("\n")
            case 3:
                print("This is the total","\n")
        if self.value_device==1:
            print("\n")
            return self.get_item()
        if self.value_device==2:
            print("\n")
            return self.get_item()
        if self.value_device==3:
            return print("Total=",round(total.sum(),2),"$")
            

if __name__ == '__main__':
    data=pd.read_excel('data_phone.xlsx',index_col=None)
    shop=GetItem()
    shop.user_selection_device()

    
            


   

