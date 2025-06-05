import tkinter as tk
import webbrowser
from tkinter import *

# Specifying the parameters of the window and setting resizing to 0,0
root = tk.Tk()
root.title("AMAP Shopping Centre")
root.geometry("1000x550")
root.resizable(0, 0)
# Static text which gets displayed to the user along its necessary parameters
Label(root, text="Welcome to AMAP Shopping Centre", font="Helvetica 24 bold").place(x=220, y=140)

def menus():
    new = Toplevel(root)
    new.title("AMAP Shopping Centre")
    new.geometry("1000x550")
    new.resizable(0, 0)
    # title for new window "Main Menus"
    Label(new, text="User Navigation Wall", font="Helvetica 18 bold").place(x=372, y=20)

    def parking():
        parking_lot = Toplevel(root)
        parking_lot.geometry("1000x550")
        parking_lot.title("AMAP Shopping Centre")
        parking_lot.resizable(0, 0)

        Label(parking_lot, text="Which car park would you like to go to?", font="Helvetica 18 bold italic").place(x=270,
                                                                                                                  y=20)

        def level_2():
            lvl2 = Toplevel(parking_lot)
            lvl2.geometry("1000x550")
            lvl2.title("AMAP Shopping Centre")
            lvl2.resizable(0, 0)
            global img

            Label(lvl2, text="How to navigate to Level 2 Car Park", font="Helvetica 18 bold italic").place(x=270, y=170)

            Label(lvl2, text="From the main car park, there are two access points at either end. Upon arrival, you can"
                             "\naccess either of them to access the shopping mall and start exploring. No matter what "
                             "\nlevel you're on, you can access the Ground Floor, Level 1 and Level 2 right from these"
                             "\naccess points.", font="Helvetica 14").place(x=100, y=250)

        Button(parking_lot, text="Level 2 Car Park", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=level_2).place(x=400, y=110)

        def level_1():
            lvl1 = Toplevel(parking_lot)
            lvl1.geometry("1000x550")
            lvl1.title("AMAP Shopping Centre")
            lvl1.resizable(0, 0)

            Label(lvl1, text="How to navigate to Level 1 Car Park", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(lvl1, text="From the ground floor, you can access the level 1 car park by either using the escalators"
                             "\nin the shopping mall directly or via the main car park entrance on the ground floor."
                             "\nFrom here, you have direct access to two access points at either end of the car"
                             "\npark to personalise your experience whilst at the shopping centre.",
                  font="Helvetica 14").place(x=130, y=230)

        Label(parking_lot, text="|==================|", font="Helvetica 18").place(x=365, y=180)
        Button(parking_lot, text="Level 1 Car Park", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=level_1).place(x=400, y=240)

        def ground_floor():
            grnd = Toplevel(parking_lot)
            grnd.geometry("1000x550")
            grnd.title("AMAP Shopping Centre")
            grnd.resizable(0, 0)

            Label(grnd, text="How to navigate to Ground Floor Car Park", font="Helvetica 18 bold italic").place(x=240,
                                                                                                                y=170)

            Label(grnd,
                  text="To navigate to the Ground Floor Car Park, you can get to it via the shopping centre stairwells"
                       "\nand elevators or via the main entrance outside. From here, there are also two access points which"
                       "\ncan be used to enter the shopping mall at either end of the car park, much like on the higher levels"
                       "\nof the car park.", font="Helvetica 14").place(x=80, y=230)

        Label(parking_lot, text="|==================|", font="Helvetica 18").place(x=365, y=310)
        Button(parking_lot, text="Ground Floor Car Park", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=ground_floor).place(x=365, y=370)

    Button(new, text="Parking", font="Helvetica 24", bg="Green", command=parking).place(x=114, y=90)

    def banks():
        bank = Toplevel(root)
        bank.geometry("1000x550")
        bank.title("AMAP Shopping Centre")
        bank.resizable(0, 0)

        Label(bank, text="Which Bank would you like to go to?", font="Helvetica 18 bold italic").place(x=270, y=20)

        def lloyds():
            bnk1 = Toplevel(bank)
            bnk1.geometry("1000x550")
            bnk1.title("AMAP Shopping Centre")
            bnk1.resizable(0, 0)

            Label(bnk1, text="How to get to Lloyds Bank", font="Helvetica 18 bold italic").place(x=350, y=180)

            Label(bnk1,
                  text="You can access Lloyds Bank on the second floor of the shopping centre. To get there, you can"
                       "\nuse escalators and elevators, depending on your level of mobility. If you are a wheelchair"
                       "\nuser, it is suggested that you use an elevator to access the second floor you can navigate to"
                       "\nLloyds Bank", font="Helvetica 14").place(x=110, y=220)

        Button(bank, text="Lloyds Bank", font="Helvetica 18", bg="NavyBlue", fg="White", command=lloyds).place(x=400,
                                                                                                               y=70)

        def hsbc_uk():
            hsbc = Toplevel(bank)
            hsbc.geometry("1000x550")
            hsbc.title("AMAP Shopping Centre")
            hsbc.resizable(0, 0)

            Label(hsbc, text="How to navigate to HSBC UK", font="Helvetica 18 bold italic").place(x=316, y=180)

            Label(hsbc, text="You can access to HSBC UK by navigating to the first second floor of the shopping centre."
                             "\nTo get there, you can use escalators or elevators depending on your level of mobility."
                             "\nIf you're a wheelchair user, it is advisable that you use an elevator so you can get to"
                             "\nthe first floor.", font="Helvetica 14").place(x=110, y=220)

        Label(bank, text="|==================|", font="Helvetica 18").place(x=340, y=125)
        Button(bank, text="HSBC UK", font="Helvetica 18", bg="NavyBlue", fg="White", command=hsbc_uk).place(x=410,
                                                                                                            y=170)

        def metro_bank():
            metro = Toplevel(bank)
            metro.geometry("1000x550")
            metro.title("AMAP Shopping Centre")
            metro.resizable(0, 0)

            Label(metro, text="How to navigate to Metro Bank", font="Helvetica 18 bold italic").place(x=310, y=170)

            Label(metro,
                  text="You access Metro Bank by navigating to the second floor of the shopping centre. To get there,"
                       "\nit is suggested that you use escalators or elevators respectively. For wheelchair users or"
                       "\nusers with poor mobility, feel free to use elevators to reach level 2 to access Metro Bank.",
                  font="Helvetica 14").place(x=100, y=210)

        Label(bank, text="|==================|", font="Helvetica 18").place(x=340, y=225)
        Button(bank, text="Metro Bank", font="Helvetica 18", bg="NavyBlue", fg="White", command=metro_bank).place(x=400,
                                                                                                                  y=265)

        def barclays():
            barc = Toplevel(bank)
            barc.geometry("1000x550")
            barc.title("AMAP Shopping Centre")
            barc.resizable(0, 0)

            Label(barc, text="How to navigate to Barclays Bank", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(barc,
                  text="You can access Barclays Bank by reaching the first floor of the shopping centre. To get there,"
                       "\nit advisable to use either an escalator or an elevator to get your destination. For wheelchair"
                       "\nor users with poorer mobility skills, feel free to use an elevator to reach your destination.",
                  font="Helvetica 14").place(x=100, y=230)

        Label(bank, text="|==================|", font="Helvetica 18").place(x=340, y=325)
        Button(bank, text="Barclays Bank", font="Helvetica 18", bg="NavyBLue", fg="White", command=barclays).place(
            x=380, y=370)

        def cbs():
            coventry = Toplevel(bank)
            coventry.geometry("1000x550")
            coventry.title("AMAP Shopping Centre")
            coventry.resizable(0, 0)

            Label(coventry, text="How to navigate to Coventry Building Society", font="Helvetica 18 bold italic").place(
                x=240, y=180)

            Label(coventry,
                  text="You can access Coventry Building Society from the ground floor. For those who parked on the upper levels"
                       "\nof the car park, you will have to use either an escalator or an elevator depending on your level of mobility."
                       "\nIf you're a user with poorer mobility or have wheelchair, it suggested that you use an elevator to descend to the"
                       "\nground floor to get to your destination.", font="Helvetica 14").place(x=30, y=230)

        Label(bank, text="|==================|", font="Helvetica 18").place(x=340, y=425)
        Button(bank, text="Coventry Building Society", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=cbs).place(x=325, y=470)

    Button(new, text="Banks", font="Helvetica 24", bg="Purple", command=banks).place(x=320, y=90)

    def shopping():
        shop = Toplevel(root)
        shop.geometry("1000x550")
        shop.title("AMAP Shopping Centre")
        shop.resizable(0, 0)

        Label(shop, text="Which type of Shop would you like to go to?", font="Helvetica 18 bold italic").place(x=250,
                                                                                                               y=20)

        def department():
            store1 = Toplevel(shop)
            store1.geometry("1000x550")
            store1.title("AMAP Shopping Centre")
            store1.resizable(0, 0)

            Label(store1, text="How to navigate all Department Stores", font="Helvetica 18 bold italic").place(x=270,
                                                                                                               y=170)

            Label(store1,
                  text="You can access all the department stores in the shopping centre by navigating the ground floor and reaching"
                       "\nthe first floor. Elevators and escalators are advised depending on your level of mobility. Wheelchair users"
                       "\nhave priority and will need use the elevators to access the higher floors of the shopping centre.",
                  font="Helvetica 14").place(x=40, y=220)

        Button(shop, text="Department Stores", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=department).place(x=230, y=70)

        def grocery():
            groc = Toplevel(shop)
            groc.geometry("1000x550")
            groc.title("AMAP Shopping Centre")
            groc.resizable(0, 0)

            Label(groc, text="How to navigate to Grocery Shops", font="Helvetica 18 bold italic").place(x=290, y=180)

            Label(groc,
                  text="You can access Grocery Shops on the ground floor. They can easily by accessed anyone, no matter"
                       "\nthe level of mobility.", font="Helvetica 14").place(x=70, y=240)

        Label(shop, text="|================|", font="Helvetica 18").place(x=220, y=125)
        Button(shop, text="Grocery Stores", font="Helvetica 18", bg="NavyBlue", fg="White", command=grocery).place(
            x=247, y=170)

        def clothing():
            clothes = Toplevel(shop)
            clothes.geometry("1000x550")
            clothes.title("AMAP Shopping Centre")
            clothes.resizable(0, 0)

            Label(clothes, text="How to navigate to Clothing Stores", font="Helvetica 18 bold italic").place(x=290,
                                                                                                             y=170)

            Label(clothes,
                  text="You can access various Clothing Stores from any floor in the shopping centre. Depending on the"
                       "\nshop, some have entrances on one or multiple floors. They can be found usually on the Ground"
                       "\nFloor, First Floor and the Second Floor of the shopping centre", font="Helvetica 14").place(
                x=80, y=230)

        Label(shop, text="|================|", font="Helvetica 18").place(x=220, y=225)
        Button(shop, text="Clothing Stores", font="Helvetica 18", bg="NavyBlue", fg="White", command=clothing).place(
            x=245, y=270)

        def accessory():
            accsry = Toplevel(shop)
            accsry.geometry("1000x550")
            accsry.title("AMAP Shopping Centre")
            accsry.resizable(0, 0)

            Label(accsry, text="How to navigate to Accessory Stores", font="Helvetica 18 bold italic").place(x=270,
                                                                                                             y=180)

            Label(accsry,
                  text="You can access Accessory Stores on the first floor and the second floor of the shopping centre."
                       "\nDepending on the company themselves, some can base themselves on the ground floor for wheelchair"
                       "\nusers to have easy access.", font="Helvetica 14").place(x=50, y=230)

        Button(shop, text="Accessory Stores", font="Helvetica 18", bg="NavyBlue", fg="White", command=accessory).place(
            x=570, y=70)

        def health():
            heal = Toplevel(shop)
            heal.geometry("1000x550")
            heal.title("AMAP Shopping Centre")
            heal.resizable(0, 0)

            Label(heal, text="How to navigate to Pharmacies", font="Helvetica 18 bold italic").place(x=300, y=180)

            Label(heal,
                  text="You can access Pharmacies almost anywhere in the shopping centre. They can be found on the"
                       "\nfirst floor, second floor or the ground floor and sometimes all three floors. Wheelchair"
                       "\nusers and users with limited motor skills can access the Pharmacies on the higher floors"
                       "\nwith elevators to assist them exploring the first and second floors of the shopping"
                       "\ncentre.", font="Helvetica 14").place(x=100, y=230)

        Label(shop, text="|================|", font="Helvetica 18").place(x=552, y=125)
        Button(shop, text="Pharmacies", font="Helvetica 18", bg="NavyBlue", fg="White", command=health).place(x=600,
                                                                                                              y=170)

        def tech():
            telecomms = Toplevel(shop)
            telecomms.geometry("1000x550")
            telecomms.title("AMAP Shopping Centre")
            telecomms.resizable(0, 0)

            Label(telecomms, text="How to navigate to Technology Stores", font="Helvetica 18 bold italic").place(x=300,
                                                                                                                 y=170)

            Label(telecomms,
                  text="You can access Technology Stores on the first and second floors. Wheelchair users and"
                       "\nusers with limited motor skills will most certainly have to use elevators elevators"
                       "\nto reach these higher floors of the shopping centre.", font="Helvetica 14").place(x=140,
                                                                                                            y=230)

        Label(shop, text="|================|", font="Helvetica 18").place(x=552, y=225)
        Button(shop, text="Technology Stores", font="Helvetica 18", bg="NavyBlue", fg="White", command=tech).place(
            x=563, y=270)

    Button(new, text="Shopping", font="Helvetica 24", bg="Orange", command=shopping).place(x=524, y=90)

    def food():
        food = Toplevel(root)
        food.geometry("1000x550")
        food.title("AMAP Shopping Centre")
        food.resizable(0, 0)

        Label(food, text="What eatery would you like to go to?", font="Helvetica 18 bold italic").place(x=280, y=20)

        def costa():
            drnk1 = Toplevel(food)
            drnk1.geometry("1000x550")
            drnk1.title("AMAP Shopping Centre")
            drnk1.resizable(0, 0)

            Label(drnk1, text="How to navigate to Costa Coffee", font="Helvetica 18 bold italic").place(x=310, y=170)
            Label(drnk1,
                  text="You can access Costa Coffee by remaining on the ground floor of the shopping centre. This"
                       "\nmeans it is accessible to wheelchair users and users with restricted motor skills who"
                       "\ncannot move around as quickly as the average person can.", font="Helvetica 14").place(x=120,
                                                                                                                y=230)

        Button(food, text="Costa Coffee", font="Helvetica 18", bg="NavyBlue", fg="White", command=costa).place(x=400,
                                                                                                               y=70)

        def starbucks():
            drnk2 = Toplevel(food)
            drnk2.geometry("1000x550")
            drnk2.title("AMAP Shopping Centre")
            drnk2.resizable(0, 0)

            Label(drnk2, text="How to navigate to Starbucks Coffee", font="Helvetica 18 bold italic").place(x=290,
                                                                                                            y=170)

            Label(drnk2,
                  text="You can access Starbucks Coffee by reaching the first floor of the shopping centre. Disabled"
                       "\nusers who have wheelchairs or restricted motor skills can use elevators to assist them"
                       "\nwith accessing the floors above them.", font="Helvetica 14").place(x=100, y=230)

        Label(food, text="|==================|", font="Helvetica 18").place(x=345, y=125)
        Button(food, text="Starbucks Coffee", font="Helvetica 18", bg="NavyBlue", fg="White", command=starbucks).place(
            x=375, y=170)

        def nero():
            drnk3 = Toplevel(food)
            drnk3.geometry("1000x550")
            drnk3.title("AMAP Shopping Centre")
            drnk3.resizable(0, 0)

            Label(drnk3, text="How to navigate to Caffe Nero", font="Helvetica 18 bold italic").place(x=310, y=170)

            Label(drnk3, text="You can access Caffe Nero by reaching either the first or second floor. To get there,"
                              "\nelevators and escalators are an option to reach your intended destination. Wheelchair"
                              "\nusers and users with restricted motor skills can also have the option to use a specialised"
                              "\nelevator that can only be used them types of people.", font="Helvetica 14").place(
                x=110, y=230)

        Label(food, text="|==================|", font="Helvetica 18").place(x=345, y=225)
        Button(food, text="Caffe Nero", font="Helvetica 18", bg="NavyBlue", fg="White", command=nero).place(x=410,
                                                                                                            y=270)

        def greggs():
            drnk4 = Toplevel(food)
            drnk4.geometry("1000x550")
            drnk4.title("AMAP Shopping Centre")
            drnk4.resizable(0, 0)

            Label(drnk4, text="How to navigate to Greggs", font="Helvetica 18 bold italic").place(x=310, y=170)

            Label(drnk4, text="You can access Greggs by remaining on the ground floor. Here, it is accessible to anyone"
                              "\nno matter the level of motor skills they have. Wheelchair users can also access Greggs"
                              "\nbut will have to be of a higher priority than the average person.",
                  font="Helvetica 14").place(x=100, y=230)

        Label(food, text="|==================|", font="Helvetica 18").place(x=345, y=325)
        Button(food, text="Greggs", font="Helvetica 18", bg="NavyBlue", fg="White", command=greggs).place(x=427, y=370)

        def jl():
            drnk5 = Toplevel(food)
            drnk5.geometry("1000x550")
            drnk5.title("AMAP Shopping Centre")
            drnk5.resizable(0, 0)

            Label(drnk5, text="How to navigate to John Lewis & Partners", font="Helvetica 18 bold italic").place(x=290,
                                                                                                                 y=170)

            Label(drnk5,
                  text="You can access John Lewis & Partners on either the ground floor, first floor or the second"
                       "\nfloor. To get to the eatery, it is suggested that you use either an escalator or an"
                       "\nelevator to get there. For wheelchair users and users with restricted motor skills,"
                       "\nfeel free to use the elevator as an alternative to using the escalator.",
                  font="Helvetica 14").place(x=140, y=230)

        Label(food, text="|==================|", font="Helvetica 18").place(x=345, y=425)
        Button(food, text="John Lewis & Partners", font="Helvetica 18", bg="NavyBlue", fg="White", command=jl).place(
            x=350, y=470)

    Button(new, text="Food", font="Helvetica 24", bg="lightBlue", command=food).place(x=750, y=90)

    def search():
        web = Toplevel(root)
        web.geometry("1000x550")
        web.title("AMAP Shopping Centre")
        web.resizable(0, 0)

        Label(web, text="What Search Engine do you want to use?", font="Helvetica 18 bold italic").place(x=260, y=20)

        def google():
            webbrowser.open("https://www.google.com/")

        Button(web, text="Google", font="Helvetica 18", bg="NavyBlue", fg="White", command=google).place(x=450, y=70)

        def bing():
            webbrowser.open("https://www.bing.com/")

        Button(web, text="Microsoft Bing", font="Helvetica 18", bg="NavyBlue", fg="White", command=bing).place(x=412,
                                                                                                               y=170)

        def ecosia():
            webbrowser.open("https://www.ecosia.org/")

        Button(web, text="Ecosia", font="Helvetica 18", bg="NavyBlue", fg="White", command=ecosia).place(x=453, y=270)

        def duckduckgo():
            webbrowser.open("https://duckduckgo.com/")

        Button(web, text="DuckDuckGo", font="Helvetica 18", bg="NavyBlue", fg="White", command=duckduckgo).place(x=417,
                                                                                                                 y=370)

    Button(new, text="Search", font="Helvetica 24", bg="Black", fg="White", command=search).place(x=114, y=220)

    Button(new, text="Disabled\nAccess", font="Helvetica 24", bg="lightBlue", command=facilities).place(x=300, y=200)

    def centre_info():
        centre = Toplevel(root)
        centre.geometry("1000x550")
        centre.title("AMAP Shopping Centre")
        centre.resizable(0, 0)

        Label(centre, text="What sort of information do you wish to seek?", font="Helvetica 18 bold italic").place(
            x=230, y=20)

        def cust_serv():
            customer = Toplevel(centre)
            customer.geometry("1000x550")
            customer.title("AMAP Shopping Centre")
            customer.resizable(0, 0)

            Label(customer, text="How to navigate to Customer Service", font="Helvetica 18 bold italic").place(x=290,
                                                                                                               y=170)

            Label(customer, text="You can access Customer Service by remaining on the ground floor. It is found to the"
                                 "\nright of the main entrance to the shopping centre and is accessible by anyone, even"
                                 "\nwheelchair users.", font="Helvetica 14").place(x=150, y=230)

        Button(centre, text="Customer Service", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=cust_serv).place(x=380, y=70)

        def help_desk():
            desk = Toplevel(centre)
            desk.geometry("1000x550")
            desk.title("AMAP Shopping Centre")
            desk.resizable(0, 0)

            Label(desk, text="How to navigate to the Help Desk", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(desk, text="You can access the Help Desk by remaining on the ground floor of the shopping centre. It"
                             "\nis also found on the right of the main entrance and next to the Customer Service.",
                  font="Helvetica 14").place(x=110, y=230)

        Label(centre, text="|==================|", font="Helvetica 18").place(x=347, y=125)
        Button(centre, text="Help Desk", font="Helvetica 18", bg="NavyBlue", fg="White", command=help_desk).place(x=420,
                                                                                                                  y=170)

    Button(new, text="Centre\nInfo", font="Helvetica 24", bg="Yellow", command=centre_info).place(x=538, y=200)

    def manual():
        user = Toplevel(root)
        user.geometry("1000x550")
        user.title("AMAP Shopping Centre")
        user.resizable(0, 0)

        Label(user, text="How to navigate the interface", font="Helvetica 18 bold italic").place(x=310, y=20)

        Label(user, text="Welcome to the user manual! This is where we provide you with assistance on how to navigate"
                         "\nthe interface and all the necessary menu systems. We'll also provide you with short snippets"
                         "\nof information describing how each menu item works.",
              font="Helvetica 14").place(x=90, y=90)

        def menu_tut():
            assist1 = Toplevel(user)
            assist1.geometry("1000x550")
            assist1.title("AMAP Shopping Centre")
            assist1.resizable(0, 0)

            Label(assist1, text="Welcome to the Menu System Tutorial", font="Helvetica 18 bold italic").place(x=270,
                                                                                                              y=20)

            Label(assist1,
                  text="To navigate the interface, you need to learn how to navigate the menu systems. There is"
                       "\na lot of menus in this app that you need to master if you don't already know how to"
                       "\nnavigate an interface."
                       "\n\nKnowing how to navigate a menu system is simply learning which buttons to how to"
                       "\ninterpret on what window each menu item points to."
                       "\n\nFor example; if you want to navigate to Parking and you want to know how."
                       "\nFirst off, you simply have to read the name of the button an interpret where you"
                       "\nthink it would take you to. Then you click it to see if it takes to that specific"
                       "\nwindow which you interpreted.", font="Helvetica 14").place(x=110, y=80)
            Label(assist1, text="Once you learn the process of interpreting where one button will take you, it becomes"
                                "\neasy and allows to replicate this process on other menu buttons you find around the app",
                  font="Helvetica 14").place(x=110, y=340)

        Button(user, text="Menu Systems Tutorial", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=menu_tut).place(x=190, y=170)

        def shop_cent_nav():
            nav = Toplevel(user)
            nav.geometry("1000x550")
            nav.title("AMAP Shopping Centre")
            nav.resizable(0, 0)

            Label(nav, text="Welcome to Shopping Centre Navigation", font="Helvetica 18 bold italic").place(x=270, y=20)

            Label(nav,
                  text="When navigating shopping centres in general, you don't really know where you are or knowing"
                       "\nwhat shops to go to if its your first time there. But for this tutorial, we'll teach you"
                       "\nhow to make your way around the shopping centre with our helpful little app."
                       "\n\nIn this app, it will tell you which floors all the shops and eateries are located so"
                       "\nyou can navigate to whichever floor the shop or eatery is on and for you to find it"
                       "\nthrough the process of elimination. Also in this app, are snippets of information for"
                       "\nwheelchair users and users with restricted motor skills who require special access points"
                       "\nreach the higher levels of the shopping centre.", font="Helvetica 14").place(x=110, y=80)
            Label(nav, text="This process can be replicated with any other shop or eatery you want to access or which"
                            "\nfloors you want to get to.", font="Helvetica 14").place(x=110, y=300)

        Button(user, text="Shopping Centre Navigation", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=shop_cent_nav).place(x=490,
                                            y=170)

    Button(new, text="Navigation\nAssist", font="Helvetica 24", bg="lightYellow", command=manual).place(x=720, y=200)


# Main Menus button that opens a child window with the User Navigation Wall
Button(root, text="Main Menus", font="Helvetica 18 bold", bg="lightBlue", command=menus).place(x=280, y=240)


def facilities():
    fac = Toplevel(root)
    fac.geometry('1000x550')
    fac.title('AMAP Shopping Centre')
    fac.resizable(0, 0)

    Label(fac, text="Facilities Wall", font="Helvetica 18 bold").place(x=417, y=20)

    def toilets():
        bog = Toplevel(root)
        bog.geometry("1000x550")
        bog.title("AMAP Shopping Centre")
        bog.resizable(0, 0)

        Label(bog, text="Which toilets do you need directions to?", font="Helvetica 18 bold italic").place(x=260, y=20)

        def lvl2_bog():
            bog2 = Toplevel(bog)
            bog2.geometry("1000x550")
            bog2.title("AMAP Shopping Centre")
            bog2.resizable(0, 0)

            Label(bog2, text="How to navigate to Level 2 Toilets", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(bog2,
                  text="You can access the Level 2 Toilets by using either escalators or elevators. Wheelchair users"
                       "\nand users with restricted motor skills should consider using elevators as an alternative"
                       "\nto escalators.", font="Helvetica 14").place(x=100, y=230)

        Button(bog, text="Level 2 toilets", font="Helvetica 18", bg="NavyBlue", fg="White", command=lvl2_bog).place(
            x=400, y=70)

        def lvl1_bog():
            bog3 = Toplevel(bog)
            bog3.geometry("1000x550")
            bog3.title("AMAP Shopping Centre")
            bog3.resizable(0, 0)

            Label(bog3, text="How to navigate to Level 1 Toilets", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(bog3, text="You can access the Level 1 Toilets by either using elevators or escalators depending on"
                             "\nyour level of mobility. For wheelchair users and users with restricted motor skills, it"
                             "\nis advisable that you use elevators to take you up to the next level of the shopping"
                             "\ncentre.", font="Helvetica 14").place(x=120, y=230)

        Label(bog, text="|==================|", font="Helvetica 18").place(x=347, y=125)
        Button(bog, text="Level 1 toilets", font="Helvetica 18", bg="NavyBlue", fg="White", command=lvl1_bog).place(
            x=400, y=170)

        def grnd_flr_bog():
            grnd2 = Toplevel(bog)
            grnd2.geometry("1000x550")
            grnd2.title("AMAP Shopping Centre")
            grnd2.resizable(0, 0)

            Label(grnd2, text="How to navigate to Ground Floor Toilets", font="Helvetica 18 bold italic").place(x=270,
                                                                                                                y=170)

            Label(grnd2,
                  text="You can access the ground floor toilets by remaining on the ground floor. They are accessible"
                       "\nto almost anyone, including disabled users. For wheelchair users, there is a specialised"
                       "\nwater cabinet which you can use as an alternative to the regular W/C.",
                  font="Helvetica 14").place(x=100, y=230)

        Label(bog, text="|==================|", font="Helvetica 18").place(x=347, y=225)
        Button(bog, text="Ground Floor toilets", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=grnd_flr_bog).place(x=365, y=270)

    Button(fac, text="Toilets", font="Helvetica 24", bg="Green", command=toilets).place(x=114, y=70)

    def wheelchair_acc():
        disabled = Toplevel(root)
        disabled.geometry("1000x550")
        disabled.title("AMAP Shopping Centre")
        disabled.resizable(0, 0)

        Label(disabled, text="Which Elevator do you require access to?", font="Helvetica 18 bold italic").place(x=250,
                                                                                                                y=20)

        def block_A():
            A = Toplevel(disabled)
            A.geometry("1000x550")
            A.title("AMAP Shopping Centre")
            A.resizable(0, 0)

            Label(A, text="How to navigate to Block A Elevator", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(A,
                  text="You can access the Block A Elevators by remaining at the front of the shopping centre. Wheelchair"
                       "\nusers and users with poorer mobility can also use these elevators that are found to the right"
                       "\nand in front of the Customer Service desk.", font="Helvetica 14").place(x=70, y=230)

        Button(disabled, text="Block A Elevator", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=block_A).place(x=390, y=70)

        def block_B():
            B = Toplevel(disabled)
            B.geometry("1000x550")
            B.title("AMAP Shopping Centre")
            B.resizable(0, 0)

            Label(B, text="How to navigate to Block B Elevator", font="Helvetica 18 bold italic").place(x=280, y=170)

            Label(B,
                  text="You can access the Block B Elevators by remaining at the front of the shopping centre. At the"
                       "\nmain entrance, turn left and you'll see them directly adjacent to the Block A Elevators."
                       "\nWheelchair users and users with poorer mobility can also use them to access other levels of"
                       "\nthe shopping centre.", font="Helvetica 14").place(x=100, y=230)

        Label(disabled, text="|=======================|", font="Helvetica 18").place(x=314, y=125)
        Button(disabled, text="Block B Elevator", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=block_B).place(x=390, y=170)

        def block_C():
            C = Toplevel(disabled)
            C.geometry("1000x550")
            C.title("AMAP Shopping Centre")
            C.resizable(0, 0)

            Label(C, text="How to navigate to Block C Elevators", font="Helvetica 18 bold italic").place(x=280, y=170)

            Label(C,
                  text="You can access the Block C Elevators by venturing to the rear of the shopping centre. From there"
                       "\nyou can access the higher levels of the shopping centre. Disabled users can also use these as"
                       "\nwell to gain access to levels 1 and 2.", font="Helvetica 14").place(x=80, y=230)

        Label(disabled, text="|=======================|", font="Helvetica 18").place(x=314, y=225)
        Button(disabled, text="Block C Elevator", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=block_C).place(x=390, y=270)

        def block_D():
            D = Toplevel(disabled)
            D.geometry("1000x550")
            D.title("AMAP Shopping Centre")
            D.resizable(0, 0)

            Label(D, text="How to navigate to Block D Elevators", font="Helvetica 18 bold italic").place(x=290, y=170)

            Label(D,
                  text="You can access the Block D Elevators by reaching the rear of the shopping centre. They are opposite"
                       "\nto the Block C Elevators so you can find and use them quickly and efficiently. Disabled users"
                       "\ncan use them as well.", font="Helvetica 14").place(x=80, y=230)

        Label(disabled, text="|=======================|", font="Helvetica 18").place(x=314, y=325)
        Button(disabled, text="Block D Elevator", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=block_D).place(x=390, y=370)

    Button(fac, text="WheelChair\nAccess", font="Helvetica 18", bg="lightBlue", command=wheelchair_acc).place(x=300,
                                                                                                              y=70)

    def baby_changing():
        baby = Toplevel(root)
        baby.geometry("1000x550")
        baby.title("AMAP Shopping Centre")
        baby.resizable(0, 0)

        Label(baby, text="How to navigate to Baby Changing facilities", font="Helvetica 18 bold italic").place(x=240,
                                                                                                               y=170)

        Label(baby,
              text="You can access Baby Changing facilities by navigating to any toilet facility in the shopping centre."
                   "\nThey can be found directly next to them and can be used by almost anyone. Disabled users can also"
                   "\nuse them as disabled toilets.", font="Helvetica 14").place(x=75, y=230)

    Button(fac, text="Baby\nChanging", font="Helvetica 18", bg="Pink", command=baby_changing).place(x=524, y=70)

    def info_points():
        info = Toplevel(root)
        info.geometry("1000x550")
        info.title("AMAP Shopping Centre")
        info.resizable(0, 0)

        Label(info, text="What Information Point do you need directions to?", font="Helvetica 18 bold italic").place(
            x=190, y=20)

        def main_info():
            main = Toplevel(info)
            main.geometry("1000x550")
            main.title("AMAP Shopping Centre")
            main.resizable(0, 0)

            Label(main, text="How to navigate to Main Entrance Information Point",
                  font="Helvetica 18 bold italic").place(x=200, y=170)

            Label(main,
                  text="You can access the Main Entrance Information Point by remaining at the main entrance of the shopping centre."
                       "\nYou can view it by standing in front of an electronic information board that consists of a map describing where"
                       "\nyou are currently and where all the nearby shops and eateries are surrounding your location.",
                  font="Helvetica 14").place(x=40, y=230)

        Button(info, text="Main entrance Information Point", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=main_info).place(x=300, y=70)

        def lvl1_info():
            lvl1_info = Toplevel(info)
            lvl1_info.geometry("1000x550")
            lvl1_info.title("AMAP Shopping Centre")
            lvl1_info.resizable(0, 0)

            Label(lvl1_info, text="How to navigate to Level 1 Information Point",
                  font="Helvetica 18 bold italic").place(x=230, y=170)

            Label(lvl1_info,
                  text="You can access the Level 1 Information Point by reaching the first floor of the shopping centre."
                       "\nTo get there, you can use either an escalator or an elevator depending on your level of mobility."
                       "\nFor wheelchair users, we suggest you use an elevator to allow you to access the first floor of the"
                       "\nshopping centre.", font="Helvetica 14").place(x=90, y=230)

        Label(info, text="|=======================|", font="Helvetica 18").place(x=314, y=125)
        Button(info, text="Level 1 Information Point", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=lvl1_info).place(x=340, y=170)

        def lvl2_info():
            lvl2_info = Toplevel(info)
            lvl2_info.geometry("1000x550")
            lvl2_info.title("AMAP Shopping Centre")
            lvl2_info.resizable(0, 0)

            Label(lvl2_info, text="How to navigate to Level 2 Information Point",
                  font="Helvetica 18 bold italic").place(x=230, y=170)

            Label(lvl2_info,
                  text="You can access the Level 2 Information Point by reaching the second floor of the shopping centre."
                       "\nTo get there, it is advisable you replicate how you got to Level 1. Whichever facility you used"
                       "\nto access Level 1 should allow to get to Level 2 with no hassles. Wheelchair users should be the"
                       "\nonly people who use elevators throughout their experience at the shopping centre.",
                  font="Helvetica 14").place(x=80, y=230)

        Label(info, text="|=======================|", font="Helvetica 18").place(x=314, y=225)
        Button(info, text="Level 2 Information Point", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=lvl2_info).place(x=340, y=270)

    Button(fac, text="Information\nPoints", font="Helvetica 18", bg="Red", command=info_points).place(x=740, y=70)

    def car_park():
        car = Toplevel(root)
        car.geometry("1000x550")
        car.title("AMAP Shopping Centre")
        car.resizable(0, 0)

        Label(car, text="Which Pay Station do you need access to?", font="Helvetica 18 bold italic").place(x=240, y=20)

        def lvl2_pay():
            pay1 = Toplevel(car)
            pay1.geometry("1000x550")
            pay1.title("AMAP Shopping Station")
            pay1.resizable(0, 0)

            Label(pay1, text="How to navigate to Level 2 Pay Station", font="Helvetica 18 bold italic").place(x=250,
                                                                                                              y=170)

            Label(pay1,
                  text="You can access the Level 2 Pay Station by using one of the two access points that lead directly"
                       "\nfrom the shopping mall to the car park. By using the stairwell or elevator depending on your level"
                       "\nof mobility, you can gain access to the Level 2 Pay Station that sits to the left of the stairwell"
                       "\nas you're coming out.", font="Helvetica 14").place(x=80, y=230)

        Button(car, text="Level 2 Pay Station", font="Helvetica 18", bg="NavyBlue", fg="White", command=lvl2_pay).place(
            x=380, y=70)

        def lvl1_pay():
            pay2 = Toplevel(car)
            pay2.geometry("1000x550")
            pay2.title("AMAP Shopping Centre")
            pay2.resizable(0, 0)

            Label(pay2, text="How to navigate to Level 1 Pay Station", font="Helvetica 18 bold italic").place(x=250,
                                                                                                              y=170)

            Label(pay2,
                  text="You can access the Level 1 Pay Station by either using one of two access points leading from the"
                       "\nshopping centre or the stairwall/elevator depending on your level of mobility. The Level 1 Pay Station"
                       "\nsits to the left of the stairwell if you use the stairwell and opposite the entrance to the shopping centre.",
                  font="Helvetica 14").place(x=80, y=230)

        Label(car, text="|=======================|", font="Helvetica 18").place(x=314, y=125)
        Button(car, text="Level 1 Pay Station", font="Helvetica 18", bg="NavyBlue", fg="White", command=lvl1_pay).place(
            x=380, y=170)

        def grnd_pay():
            pay3 = Toplevel(car)
            pay3.geometry("1000x550")
            pay3.title("AMAP Shopping Centre")
            pay3.resizable(0, 0)

            Label(pay3, text="How to navigate to Ground Floor Pay Station", font="Helvetica 18 bold italic").place(
                x=240, y=170)

            Label(pay3,
                  text="You can access the Ground Floor Pay Station by navigating to the ground floor of the shopping centre"
                       "\nif you are not already. Depending on your level of mobility, you can use either escalators or elevators"
                       "\nto get to the ground floor. Using one of the two access points, you navigate to the ground floor of the car"
                       "\npark. The Pay Station is to the left, next to the stairwell.", font="Helvetica 14").place(
                x=60, y=230)

        Label(car, text="|=======================|", font="Helvetica 18").place(x=314, y=225)
        Button(car, text="Ground Floor Pay Station", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=grnd_pay).place(x=340, y=270)

    Button(fac, text="Car Park\nPay Stations", font="Helvetica 18", bg="Black", fg="White", command=car_park).place(
        x=95, y=200)

    def support():
        help = Toplevel(root)
        help.geometry("1000x550")
        help.title("AMAP Shopping Centre")
        help.resizable(0, 0)

        Label(help, text="Which Help Desk do you want directions to?", font="Helvetica 18 bold italic").place(x=240,
                                                                                                              y=20)

        def lvl2_help():
            lvl2 = Toplevel(help)
            lvl2.geometry("1000x550")
            lvl2.title("AMAP Shopping Centre")
            lvl2.resizable(0, 0)

            Label(lvl2, text="How to navigate to Level 2 Help Desk", font="Helvetica 18 bold italic").place(x=270,
                                                                                                            y=170)

            Label(lvl2,
                  text="You can access the Level 2 Help Desk by reaching the second level of the shopping centre. To get there,"
                       "\nyou can use either escalators or elevators depending on your level of mobility. Wheelchair users have"
                       "\npriority when using elevators as they have restricted motor skills.",
                  font="Helvetica 14").place(x=50, y=230)

        Button(help, text="Level 2 Help Desk", font="Helvetica 18", bg="NavyBlue", fg="White", command=lvl2_help).place(
            x=380, y=70)

        def grnd_help():
            ground = Toplevel(help)
            ground.geometry("1000x550")
            ground.title("AMAP Shopping Centre")
            ground.resizable(0, 0)

            Label(ground, text="How to navigate to the Ground Floor Help Desk", font="Helvetica 18 bold italic").place(
                x=240, y=170)

            Label(ground,
                  text="You can access the Ground Floor Help Desk by making your way towards the Customer Service Desk."
                       "\nThe Help Desk is located opposite the Customer Service Desk to the right of the main entrance"
                       "\nof the shopping centre. Wheelchair users can also access this help desk because it is on the"
                       "\nground floor.", font="Helvetica 14").place(x=80, y=230)

        Label(help, text="|=======================|", font="Helvetica 18").place(x=314, y=125)
        Button(help, text="Ground Floor:Main Entrance\nHelp Desk", font="Helvetica 18", bg="NavyBlue", fg="White",
               command=grnd_help).place(x=320, y=170)

    Button(fac, text="Help Desk", font="Helvetica 20", bg="Yellow", command=support).place(x=300, y=200)


Button(root, text="Facilities Required", font="Helvetica 18 bold", bg="lightBlue", command=facilities).place(x=470,
                                                                                                             y=240)

# Execute Tkinter
root.mainloop()
