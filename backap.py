from tkinter import *
import time 
import backend
import difflib
from difflib import get_close_matches
from collections import Counter
import itertools
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

master = Tk()

backend.create_table_diet()


def add_command():
    list2.insert(END, mynamefordiet)

    backend.InsertIntoDiet(mynamefordiet)
    print(backend.ViewDiet())

def delete_command():
    
    index = list2.curselection()
    print (index[0]) # to jest index, duuh
    
    myitem = (backend.ViewDiet()[index[0]][1]) # var used to refer selected item

    backend.DeleteFromDietByName(myitem) # delete item in list 
    list2.delete(index[0]) # remove name from gui

    print(backend.ViewDiet())

def prop(n):
    return 360.0 * n /1000

def myselection4(event):
    index = list2.curselection()
    print (backend.FindItemWithName(backend.ViewDiet()[index[0]][1])) # acces all info for item with given name

def myselection2(event):

    index = list1.curselection()
    index = (int(','.join(str(v) for v in index)))
    
    #print (idsofsearch)
    #for i in idsofsearch:
    #    print (backend.ViewAllWithId(i))
    #print (idsofsearch[index])

    #to powinno wskazac wszystko z indexem z idsofsearch trzeba podzielic i zformatowac by wygladalo jak sel name
    GetGroupList= backend.ViewAssignedFoodGroup(dropmenu.get()) # all names of selected food group
    global selected_name
    selected_name = ()
    if dropmenu.get() == "Search Results":
        
        selected_namealt = backend.ViewAllWithId((idsofsearch[index]))
        selected_name = selected_namealt
    else:
        selected_name = GetGroupList[index]

     # selected name in lit with a index

    selected_name = str(selected_name)
    toto = (str(selected_name)).translate({ord(i):None for i in ",'[]"}) #var used to find * in table handles brackets in names
    selected_name = (str(selected_name)).translate({ord(i):None for i in ",()'"}) #selected name to string and make it nice
    SelectedList = (backend.FindItemWithName(toto[1:-1])) #list nutrients in selected item
    
    SelectedList = (str(SelectedList))
    SelectedList = SelectedList.translate({ord(i):None for i in "('][)"})
    SelectedList = list(SelectedList.split(","))

    SelectedListProper = (SelectedList[2:])
    
    #print ("index is : ",index)
    #print ("Selected name  is : ", selected_name,"and its class is", type(selected_name))
    #print (SelectedListProper)
    global mynamefordiet
    mynamefordiet = selected_name

    t1.delete(0.0, END)
    t1.insert(END, selected_name)

    plt.close("all")

    for i in range(len(master.entryWidgets)):
        master.entryWidgets[i].delete(0, END)
        master.entryWidgets[i].insert(END, SelectedListProper[i])
    
    #make weight normalized mg 
    myvaro = SelectedList[3:]
    mypienozeros = []
    for i in range(len(myvaro)):#change none to 0 so there is no issues in math later on
        if myvaro[i] != " None":
            mypienozeros.append(myvaro[i])
        else:
            myvaro[i] = 0
            mypienozeros.append(myvaro[i])
    #print (mypienozeros[0:]) # tego chce uzyc do obliczania procent rws
    #TEST
    #zakladam wage 80kg porcent = 100.*values/values.sum()
    for i in range(len(mypienozeros[0:])):
        master.EntryWidgetsRwsPercent[i].delete(0, END)
        if i == 0 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/2000)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #calories 2000
        elif i == 1 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/70)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#fat 70g na 2000kcal
        elif i == 2 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/80)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#protein 1g na kg masy = 80g
        elif i == 3 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/130)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#carbo 130g
        elif i == 4 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/25)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#sugar <25g
        elif i == 5 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/300)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #cholesterol <300mg
        elif i == 6 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/30)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#csaturated fats <30g
        elif i == 7 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/1000)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #calcium 1000mg
        elif i == 8 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/18)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#iron 18mg
        elif i == 9 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/3500)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#potas 3500mg
        elif i == 10 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/400)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #magnesiumk 400mg
        elif i == 11 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/5000)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#vitamin A 5000iu
        elif i == 12 and mypienozeros[0:][i] != 0:
            a= ((float(mypienozeros[0:][i])/60)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#vitamin c 60mg
        elif i == 13 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.006)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#vitamin b12 0.006 mg / given value  in mcg
        elif i == 14 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.01)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#vitamin D 0.01mg
        elif i == 15 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/2400)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #sodium 2400mg
        elif i == 16 and mypienozeros[0:][i] != 0:
            a= ((float(mypienozeros[0:][i])/15)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#zinc 15mg
        elif i == 17 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/5)*100))
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #manganese 5mg
        elif i == 18 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1.5)*100))
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#b1 1.5mg
        elif i == 19 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1.7)*100))
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#b2 1.7mg
        elif i == 20 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/20)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#b3 20mg
        elif i == 21 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/10)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#b5 10mg
        elif i == 22 and mypienozeros[0:][i] != 0:
            a = ((float(mypienozeros[0:][i])/2)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#b6 2mg
        elif i == 23 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.3)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#b7 0.3mg / given value  in mcg
        elif i == 24 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.4)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}')) #b9 0.4mg / given value  in mcg
        elif i == 25 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.05)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#d2 0.05mg / given value  in mcg
        elif i == 26 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.025)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#d3 0.025mg / given value  in mcg
        elif i == 27 and mypienozeros[0:][i] != 0:
            a = (((float(mypienozeros[0:][i])/1000)/0.08)*100)
            master.EntryWidgetsRwsPercent[i].insert(END, (f'{a:.2f}'))#K 0.08mg / given value  in mcg
        else:
            None
    
    truepie = []
    for i in range(len(mypienozeros)):#change none to 0 so there is no issues in math later on
        if i in [1,2,3,4]: #change g to mg 
            truepie.append((float(mypienozeros[i]))*1000)
        elif i == 5: #just append 
            truepie.append(float(mypienozeros[i]))
        elif i == 6:#change g to mg 
            truepie.append((float(mypienozeros[i]))*1000)
        elif i in [7,8,9,10]: #just append 
            truepie.append(float(mypienozeros[i]))
        elif i == 11:
            truepie.append((float(mypienozeros[i]))*0.3/1000)# change iu to mcg and to mg
        elif i == 12:
            truepie.append(float(mypienozeros[i]))#just append
        elif i == 13 or i == 14:
            truepie.append((float(mypienozeros[i]))/1000)#mcg to mg
        elif i in[15,16,17,18,19,20,21,22]:
            truepie.append(float(mypienozeros[i]))#just append
        elif i == 23 or i == 24 or i == 25 or i == 26 or i == 27:
            truepie.append((float(mypienozeros[i]))/1000)#mcg to mg
    #print(truepie)
    #make dicto for piechart and legend
    mydataforpie = (listofcolumns[2:])
    #print(mydataforpie)
    dictopie = {}
    
    for i in range(0, len(mydataforpie)):
        dictopie.update({(truepie[i]):(mydataforpie[i])})
    #print (dictopie)

    #get list of selected item  for pie chart and remove nones and zeros
    piechartdata = {} 
       
    for i in range(0, len(dictopie)):
        if (list(dictopie.keys())[i]) != 0 and (list(dictopie.keys())[i]) != 0.0:
            piechartdata.update({(list(dictopie.keys())[i]):(list(dictopie.values())[i])})
    #print(piechartdata)
    #count % of chart
    piepercent = [(i/(sum(piechartdata))*100) for i in piechartdata]
    piepercent = sorted(piepercent) # gotta to sort that form low to high

    #labe = [(i) for i in list(piechartdata.values())]
    #values = [(i) for i in list(piechartdata.keys())]
    labe = np.char.array([(i) for i in list(piechartdata.values())])
    values = np.array([(i) for i in list(piechartdata.keys())])
    porcent = 100.*values/values.sum()

    labels = ['{0} - {1:1.5f} %'.format(i,j) for i,j in zip(labe, porcent)]

    #  explode=(0, 0.05, 0, 0)
    # as explode needs to contain numerical values for each "slice" of the pie chart (i.e. every group needs to have an associated explode value)
    explode = list()
    for label in labels:
        explode.append(0.1)
    # now to get the total number of failed in each section

    actualFigure = plt.figure(figsize = (7,7))
    actualFigure.suptitle("Percentage Of Nutritional Value", fontsize = 22)

    pie = plt.pie(values, labels=labels, explode=explode, shadow=False, labeldistance=None,) #autopct='%1.1f%%' pctdistance = 1.4
    plt.legend(pie[0], labels, loc="lower left",fontsize=8,bbox_to_anchor=(-.15, -.1))
    global o #?
    try:
        o.get_tk_widget().destroy()
    except:
        None
    o = FigureCanvasTkAgg(actualFigure,master)
    o.get_tk_widget().grid_forget()
    o.get_tk_widget().grid(row=1, column=10,rowspan=30)
    

def callback(*args):
    list1.delete(0, END)
    for choosenitem in backend.ViewAssignedFoodGroup(dropmenu.get()):
        choosenitem = (','.join(str(v) for v in choosenitem))
        list1.insert(END, choosenitem)

def test_command():
    mylist = [backend.View()]#import all names as list with single item
    iteminlist = ((str(mylist)).split(", "))#split items by coma
    myname = (mytextvar.get().title())
    global idsofsearch
    idsofsearch = []
    dropmenu.set("Search Results")
    list1.delete(0, END)
    for i in iteminlist:
        if myname in i:
            list1.insert(END, i)
            mysearchvar= backend.FindItemWithName(i[2:-3]) #find item with name but remove qotation marks and brackets # returns a string
            searchvarlist = ((str(mysearchvar)).split(", "))#split string by comas
            idsofsearch.append(searchvarlist[0][2:])#add ids one by one to list # ignores name and calories
        else:
            None

#search enginge test

mytextvar = StringVar()
e1=Entry(master, width=50, textvariable= mytextvar)
e1.grid(row=34,column=11,)
e1.focus_set()

mytextvar.set("Search")
searchvalue = mytextvar.get()

#empty canvas for pie chart
w = Canvas(master, width=700, height=700)
w.grid(row=1, column=10,rowspan=30)

#dROP DOWN MENU

FoodGroups = [(i) for i in backend.ViewAllFoodGroups()]
FoodGroups = set(FoodGroups)
FoodGroups = list(itertools.chain.from_iterable(FoodGroups))

#remove nons from the list
allfoodgroups = [] 
for i in FoodGroups: 
    if i != None : 
        allfoodgroups.append(i) 
#sort aplhabetipiply
allfoodgroups = sorted(allfoodgroups)

#define variable
dropmenu = StringVar(master)
dropmenu.set("Fish") # default value
dropmenu.trace("w", callback)

dropmenuwidgets = [i for i in allfoodgroups]

w = OptionMenu(*(master, dropmenu) + tuple(allfoodgroups))
w.grid(row=32, column=11,)

b2=Button(master, text="Search",command = test_command)
b2.grid(row=33,column=11)

b3=Button(master, text="ADD TO DIET",command = add_command)
b3.grid(row=33,column=13)

b4=Button(master, text="REMOVE FROM DIET",command = delete_command)
b4.grid(row=34,column=13)

#check lenght of name list
a_list = backend.View()
characterscount1 = str(max(a_list, key=len))
lenghtoflist1 = int(len(characterscount1))

#label for percentage of rws
percentofrwslabel = Label(master, text = "% of RWS")
percentofrwslabel.grid(row=1, column=7)

#texts in column 2
t1= Text(master,height=1, width=lenghtoflist1)
t1.grid(row=0,column=2,columnspan = 10)

#define lists
list1=Listbox(master,exportselection=False, height = 50, width = lenghtoflist1,)
list1.grid(row=1,column=11, rowspan = 30,)

list2=Listbox(master,exportselection=False, height = 50, width = lenghtoflist1)
list2.grid(row=1,column=13, rowspan = 30)

#define scrollbar
sb1=Scrollbar(master)
sb1.grid(row=1,column=12,rowspan=30, sticky='ns')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#binding
list1.bind('<<ListboxSelect>>', myselection2)
list2.bind('<<ListboxSelect>>', myselection4)
#add labels and entry widgets for items
allrows = backend.ViewAllRows()

listofcolumns = [(i[1]) for i in allrows[2:]]
listofweight = ["Unit","Cal","g","g","g","g","mg","g","mg","mg","mg","mg","iu","mg","mcg","mcg","mg","mg","mg","mg","mg","mg","mg","mg","mcg","mcg","mcg","mcg","mcg","mcg",]
rwsvalues = ["RWS","2000kcal","70g/2000kcal","1g/kg masy","130g","<25g","<300 mg","<30g","1000 mg ","18 mg","3500 mg","400mg","5000 iu","60 mg","0.006 mg","0,01 mg","2400mg","15 mg","5mg","1.5 mg","1.7 mg","20mg","10mg","2mg","0.3 mg","0.4 mg","0.05 mg","0.025 mg","0,08mg",]


master.entryWidgets = []
labelWidgets = []
labelWidgets2 = []
labelWidgets3 = []
master.EntryWidgetsRwsPercent = []

for i in range(0, len(listofcolumns)):
    #make widgets
    labelWidgets.append(Label(master, text = listofcolumns[i]))
    labelWidgets2.append(Label(master, text = listofweight[i]))
    master.entryWidgets.append(Entry(master, width=10))
    
    
    #location of widgets
    labelWidgets[-1].grid(row= i+1, column =2, sticky='e')
    labelWidgets2[-1].grid(row= i+1, column =4, sticky='e')
    master.entryWidgets[-1].grid(row= i+1, column = 3, sticky='w')
    
for i in range(0, len(listofcolumns)):
    labelWidgets3.append(Label(master, text = rwsvalues[i]))
    labelWidgets3[-1].grid(row= i+1, column =5,columnspan=2)
    



for i in range(1, len(listofcolumns)):
    master.EntryWidgetsRwsPercent.append(Entry(master, width=10))
    master.EntryWidgetsRwsPercent[-1].grid(row= i+1, column = 7, sticky='w')


list2.delete(0, END)
for i in backend.ViewDiet():
    list2.insert(END, i)



master.mainloop()







