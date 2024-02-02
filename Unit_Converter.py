#Lenght
def met_feet(x):
    #Converts the value entered in metters into feets
    a = x*3.3
    return a

def in_cm(x):
    #Converts the value entered in inch into centimeters
    b = x*2.43
    return b

def mi_km(x):
    #Converts the value entered in miles into kilometers
    c = x*1.61
    return c

#Temperature
def cels_far(x):
    #Converts Celsius to Fahrenheit
    d = 9/5*x+32
    return d

def far_cels(x):
    #Converts Fahrenheit to Celsius
    e = 5/9*(x-32)
    return e

def cels_kel(x):
    #Converts Celsius to Kelvin
    f = x +273.15
    return f

def far_kel(x):
    #Converts Farenhreit to Kelvin
    g = 5/9*(x-32)+273.15
    return g

#Mass
def kg_lb(x):
    #Converts kg in lb
    h = x*2.2
    return h

def oz_g(x):
    #Converts oz to g
    i = x*28.35
    return i

def ft_m(x):
    #Converts oz to g
    j = x*0.028
    return j

#Volume
def ml_cc(x):
    #Converts ml to cc (ml=cc)
    return x

def cup_ml(x):
    """Converts cup to ml """
    k = x*237
    return k

def gal_c(x):
    """Converts gal to c"""
    l = x*16
    return l

def m3_ft3(x):
    """Converts m3 to ft3"""
    m = x*35.31
    return m

#Pressure

def atm_kPa(x):
    """Converts atm to kPa"""
    n = x*101.3
    return n

def atm_mmHG(x):
    """Converts atm to mm Hg"""
    o = x*760
    return o

def bar_Pa(x):
    """Converts bar to Pa"""
    p = x*pow(10, 5)
    return p

def psi_mbar(x):
    """Converts psi to mbar"""
    q = x*68.948
    return q

#Energy

def J_kcal(x):
    """Converts J to kcal"""
    r = x*(2.39*pow(10, -4))
    return r

def eV_K(x):
    """Converts eV to K"""
    s  = x*(1.602*pow(10, -19))
    return s



conv_menu_length = "1-m/ft\n2-in/cm\n3-mi/km\nexit\nPlease select the conversion or exit for the main menu: "
conv_menu_temp = "1-Celsius/Fahr\n2-Fahr/Celsius\n3-Celsius/Kelvin\n4-Fahr/Kelvin\nexit\nPlease select a conversion or exit for main menu: "
conv_menu_mass = "1-Kg/Lb\n2-Oz/g\n3-Ft/m\nexit\nPlease select a conversion or exit for the main menu: "
conv_menu_volume = "1-ml/cc\n2-cup/ml\n3-gal/c\n4-m3/ft3\nexit\nPlease select a conversion or exit for the main menu: "
conv_menu_pressure = "1-atm/kPa\n2-atm/mmHG\n3-bar/Pa\n4-Psi/mbar\nexit\nPlease select a conversion or exit for the main menu: "
conv_menu_energy = "1-J/kcal\n2-eV/K\nexit\nPlease select a conversion or exit for the main menu: "



while True:
    main_menu = "1-Length\n2-Temperature\n3-Mass\n4-Volume\n5-Pressure\n6-Energy\nexit\nPlease select the unit you`d like to convert or exit to close the program: "
    unit = input(main_menu) #It allows the user to select one section out of the whole menu

    while True:
         if unit == '1':
            conv_menu = conv_menu_length
         elif unit == '2':
            conv_menu = conv_menu_temp
         elif unit == '3':
            conv_menu = conv_menu_mass
         elif unit == '4':
            conv_menu = conv_menu_volume
         elif unit == '5':
            conv_menu = conv_menu_pressure
         elif unit == "6":
            conv_menu = conv_menu_energy
         elif unit == "exit":
             break
         conv = input(conv_menu)   #It allows the user to select 1 conversion out of the section menu
         if conv == 'exit':  #step back to the main menu
             break

         while True:

            x = eval(input("Enter your value: "))
            list_length = [met_feet(x), in_cm(x), mi_km(x)]
            list_temp = [cels_far(x), far_cels(x), cels_kel(x), far_kel(x)]
            list_mass = [kg_lb(x), oz_g(x), ft_m(x)]
            list_volume = [ml_cc(x), cup_ml(x), gal_c(x), m3_ft3(x)]
            list_pressure = [atm_kPa(x), atm_mmHG(x), bar_Pa(x), psi_mbar(x)]
            list_energy = [J_kcal(x), eV_K(x)]
            #After choosing the unit, the conversions section will take the proper list to work with
            if unit == '1':
                conversions = list_length
            elif unit == '2':
                conversions = list_temp
            elif unit == '3':
                conversions = list_mass
            elif unit == '4':
                conversions = list_volume
            elif unit == '5':
                conversions = list_pressure
            elif unit == "6":
                conversions = list_energy


            #According to user`s choice will select the element from the list
            if conv == '1':
                ans = conversions[0]
            elif conv == '2':
                ans = conversions[1]
            elif conv == '3':
                ans = conversions[2]
            elif conv == '4':
                ans = conversions[3]


            #Allows user to do endless operations with the same conversion
            print(f"Value converted is:  {ans}")
            question = "Would you like other conversion in here? (yes or no): "
            user = input(question)
            if user == 'no':   #or to change to another one
                break

    if unit == 'exit':   #Close the program
        print("See you next time!")
        break
