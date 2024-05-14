
import pandas as pd
from tabulate import tabulate
from enum import Enum

"""
    This is what RT Weapon Scraper generated. WTF
    Hardpoint Type,Weapon Class,Weapon Name,Indirectfire,Clustering Capable (Weapon or with ammo),Tonnage,Slots,
    Max Recoil,Base Direct Damage,Max Direct Damage,Max Bonus Ammo Damage,
    Highest Direct Damage Ammo (Comparing Damage Bonus/Multiplier), AOE Damage,AOE Heat Damage,AOE Radius,
    Highest Bonus AOE Ammo,Damage Variance,Max Stability Damage,Max Heat Damage,Max Per Ammo Heat Damage,
    Highest Direct Heat Damage Ammo,Max Firing Heat,Max Jam Chance,Can Misfire,Damage Per Heat,Damage Per Slot,
    Damage Per Ton,Weapon Crit Multiplier,Weapon Base Crit Chance,Weapon TAC Chance (50% Max Thickness),
    Max TAC Armor Thickness,Base Accuracy Bonus,Base Evasion Ignore,Min Range,Short Range,Medium Range,
    Long Range,Max Range,Damage Falloff %,Min Range Damage,Short Range Damage,Medium Range Damage,Long Range Damage,
    Max Range Damage,Weapon AAA Factor %
    """

class Hardpoint(Enum):
    Missile = 1
    Ballistic = 2
    Energy = 3
    AntiPersonnel = 4 # really?

class WeaponClass(Enum):  # better to code hardpoint type in there (is that even possible?)
    Autocannon = 1  # ballistic
    Flamer = 2      # energy
    Gauss = 3       # ballistic
    Laser = 4       # energy
    LRM = 5         # missile
    MachineGun = 6  # ballistic
    PPC = 7         # energy
    SRM = 8         # srm

indices = [
    "hardpoint",    # ???- hardpoint type ('Missile')
    "class",        # ??? - weapon class ('LRM', 'Autocannon', ...)
    "name",         # str - 'ATM-9 (C)'
    "tonnage",      # int - 7t
    "slots",        # int - 5
    "min", "short", "medium", "long", "max", # int - weapon ranges
    ]

data_atm9c = [Hardpoint.Missile, WeaponClass.LRM, 'ATM-9 (C)',
            7, 5, 120, 150, 300, 450, 600]
data_ac10 = [Hardpoint.Ballistic, WeaponClass.Autocannon, 'AC/10',
             12, 5, 0, 150, 300, 450, 600]

if __name__ == "__main__":

    df = pd.DataFrame(columns=indices)
    print(df)
    ## add values by index

    ## add rows
    df1 = pd.DataFrame([data_atm9c], columns=indices)
    df2 = pd.DataFrame([data_ac10], columns=indices)
    df = pd.concat([df, df1])  # missile
    df = pd.concat([df, df2])  # ac10

    # HOW TO PRINT
    # https://www.geeksforgeeks.org/how-to-print-an-entire-pandas-dataframe-in-python/
    # https://www.geeksforgeeks.org/display-the-pandas-dataframe-in-table-style/
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    print(df.iloc[[0]])         # missile
    print(type(df.iloc[[0]]))   # <class 'pandas.core.frame.DataFrame'>

    # todo:ADD code to read the columns and add them to the dataframe
    #  https://www.geeksforgeeks.org/creating-a-pandas-dataframe/?ref=next_article