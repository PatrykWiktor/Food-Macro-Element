#import pandas as pd
import sqlite3


#fooddata = pd.read_excel('Fooddata.xlsx', sheet_name=0,header=0)
#fooddata.to_sql('foodtable', conn, if_exists='append', index=False)

def create_table():
    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS foodtable (ID INTEGER PRIMARY KEY , Name TEXT, FoodGroup TEXT, Calories INTEGER, Fat REAL, Protein REAL, Carbohydrate REAL, Sugars REAL, Cholesterol REAL, SaturatedFats REAL, Calcium INTEGER, Iron REAL, Potassium INTEGER, Magnesium INTEGER, VitaminA INTEGER, VitaminC REAL, VitaminB12 REAL, VitaminD REAL, Sodium INTEGER, Zinc REAL, Manganese REAL, ThiaminB1 REAL, RiboflavinB2 REAL, NiacinB3 REAL, PantothenicacidB5 REAL, VitaminB6 REAL, BiotinB7 REAL, FolateB9 REAL, VitaminD2 REAL, VitaminD3 REAL, VitaminK REAL)")
    conn.commit()
    conn.close()

def create_table_diet():
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS diettable (ID INTEGER PRIMARY KEY , Name TEXT)")
    conn.commit()
    conn.close()

def ViewDiet():
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * from diettable")
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewInDiet(ID):
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT Name from diettable WHERE ID=?",(ID,))
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewInDietByName(Name):
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * from diettable WHERE Name=?",(Name,))
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def InsertIntoDiet(Name):
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO diettable VALUES (NULL,?)",(Name,))
    conn.commit()
    conn.close()

def DeleteFromDiet(id):
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM diettable WHERE id=?",(id,))
    conn.commit()
    conn.close()

def DeleteFromDietByName(Name):
    conn = sqlite3.connect("dietdatabase.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM diettable WHERE Name=?",(Name,))
    conn.commit()
    conn.close()

def View():

    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT Name from foodtable")
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewAssignedFoodGroup(group):
    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT Name from foodtable WHERE FoodGroup= (?)", (group,))
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewAllFoodGroups():

    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT FoodGroup from foodtable")
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewName(index):
    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT Name from foodtable WHERE rowid= (?)", (index,))
    choosenitem = cur.fetchall()
    choosenitem = (''.join(str(v) for v in choosenitem))
    conn.close()
    return choosenitem

def GetAllInfo(index):
    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * from foodtable WHERE ID= (?)", (index,))
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewAllRows():

    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute ("PRAGMA table_info(foodtable)")
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewAllWithId(id): #find item with id of "?"

    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT Name from foodtable where ID = (?)", (id,)) 
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def FindItemWithName(name):
    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * from foodtable where Name = (?)", (name,))
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

def ViewAllWithId2(num,grupa): #find item with id of "?"

    conn = sqlite3.connect("fooddatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * from foodtable where ID = (?) AND FoodGroup = (?)", (num, grupa,)) # and food group is dropmenu.get
    choosenitem = cur.fetchall()
    conn.close()
    return choosenitem

