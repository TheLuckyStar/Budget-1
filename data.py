from gi.repository import Gtk, Gio
from decimal import *
import os.path 

class Data():

    def __init__(self):
        #Indexes for data arrays
        self.CATEGORY = 0
        self.CATEGORY_INDEX = 0
        self.CATEGORY_TEXT = 1

        self.DATE = 1
        self.DATE_YEAR = 0
        self.DATE_MONTH = 1
        self.DATE_DAY = 2
       
        self.VALUE = 2
        self.DESCRIPTION = 3
        
        self.UNIQUE_ID = 4 

        self.LATEST_ID = 0

        self.incomeMenu = []
        self.expenseMenu = []
        self.currentMonthMenu = []
        self.allMonthMenu = []
        self.income = []
        self.expenses = []

    def import_data(self):
        if(os.path.isfile('database.txt')):
            f = open('database.txt', 'r')
            for db in f.readlines():
                line = db.split(',')
                if line[0] == 'incomeMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.arr.append(line[3].strip())
                    self.incomeMenu.append(self.arr)
                elif line[0] == 'expenseMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.arr.append(line[3].strip())
                    self.expenseMenu.append(self.arr)
                elif line[0] == 'currentMonthMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.currentMonthMenu.append(self.arr)
                elif line[0] == 'allMonthMenu':
                    self.arr = []
                    self.arr.append(int(line[1].strip()))
                    self.arr.append(line[2].strip())
                    self.allMonthMenu.append(self.arr)
                elif line[0] == 'income':
                    self.arr = []
                    self.catArr = []
                    self.DATEArr = []
                    self.catArr.append(int(line[1].strip()))
                    self.catArr.append(line[2].strip())
                    self.DATEArr.append(int(line[3].strip()))
                    self.DATEArr.append(int(line[4].strip()))
                    self.DATEArr.append(int(line[5].strip()))
                    self.arr.append(self.catArr)
                    self.arr.append(self.DATEArr)
                    self.arr.append(Decimal(line[6].strip()))
                    self.arr.append(line[7].strip())
                    self.arr.append(line[8].strip())
                    if self.LATEST_ID < int(line[8].strip()):
                        self.LATEST_ID = int(line[8].strip())
                    self.sort_data(self.income)

                elif line[0] == 'expense':
                    self.arr = []
                    self.catArr = []
                    self.DATEArr = []
                    self.catArr.append(int(line[1].strip()))
                    self.catArr.append(line[2].strip())
                    self.DATEArr.append(int(line[3].strip()))
                    self.DATEArr.append(int(line[4].strip()))
                    self.DATEArr.append(int(line[5].strip()))
                    self.arr.append(self.catArr)
                    self.arr.append(self.DATEArr)
                    self.arr.append(Decimal(line[6].strip()))
                    self.arr.append(line[7].strip())
                    self.arr.append(line[8].strip())
                    if self.LATEST_ID < int(line[8].strip()):
                        self.LATEST_ID = int(line[8].strip())
                    self.sort_data(self.expenses)
            
            f.close()

    def sort_data(self, data):
        if len(data) == 0:
            data.append(self.arr)
        else:
            flag = False
            for i in range(len(data)):
                # If entry's year is equal to array's year
                if data[i][self.DATE][self.DATE_YEAR] == int(self.arr[self.DATE][self.DATE_YEAR]):
                    # If entry's month is equal to array's month
                    if data[i][self.DATE][self.DATE_MONTH] == int(self.arr[self.DATE][self.DATE_MONTH]):
                        # If entry's day is equal to array's day
                        if data[i][self.DATE][self.DATE_DAY] == int(self.arr[self.DATE][self.DATE_DAY]):
                            #self.expenses.insert(i, self.arr)
                            flag = True
                            break
                        # If entry's day is less than array's day
                        elif data[i][self.DATE][self.DATE_DAY] < int(self.arr[self.DATE][self.DATE_DAY]):
                            data.insert(i , self.arr)
                            flag = True
                            break
                    # If entry's month is less than array's month
                    elif data[i][self.DATE][self.DATE_MONTH] < int(self.arr[self.DATE][self.DATE_MONTH]):
                        data.insert(i - 1 , self.arr)
                        flag = True
                        break
                # If entry's year is less than income array's year
                elif data[i][self.DATE][self.DATE_YEAR] < int(self.arr[self.DATE][self.DATE_YEAR]):
                    data.insert(i , self.arr)
                    flag = True
                    break

            if flag == False:
                data.append(self.arr)
            

    def add_data(self, entryString):
        if(os.path.isfile('database.txt')):
            f = open('database.txt', 'a')
            f.write(entryString)
            f.close()

    def translate_date(self,data,index):
        dateString = ""
        
        if data[index][self.DATE][self.DATE_MONTH] == 1:
            dateString += ("January")
        elif data[index][self.DATE][self.DATE_MONTH] == 2:
            dateString += ("February")
        elif data[index][self.DATE][self.DATE_MONTH] == 3:
            dateString += ("March")
        elif data[index][self.DATE][self.DATE_MONTH] == 4:
            dateString += ("April")
        elif data[index][self.DATE][self.DATE_MONTH] == 5:
            dateString += ("May")
        elif data[index][self.DATE][self.DATE_MONTH] == 6:
            dateString += ("June")
        elif data[index][self.DATE][self.DATE_MONTH] == 7:
            dateString += ("July")
        elif data[index][self.DATE][self.DATE_MONTH] == 8:
            dateString += ("August")
        elif data[index][self.DATE][self.DATE_MONTH] == 9:
            dateString += ("September")
        elif data[index][self.DATE][self.DATE_MONTH] == 10:
            dateString += ("October")
        elif data[index][self.DATE][self.DATE_MONTH] == 11:
            dateString += ("November")
        elif data[index][self.DATE][self.DATE_MONTH] == 12:
            dateString += ("December")
        else:
            dateString += ("Month Fail")

        dateString += (" " + str(data[index][self.DATE][self.DATE_DAY]))

        if data[index][self.DATE][self.DATE_DAY] == 1:
            dateString += ("st")
        elif data[index][self.DATE][self.DATE_DAY] == 21:
            dateString += ("st")
        elif data[index][self.DATE][self.DATE_DAY] == 31:
            dateString += ("st")
        elif data[index][self.DATE][self.DATE_DAY] == 2:
            dateString += ("nd")
        elif data[index][self.DATE][self.DATE_DAY] == 22:
            dateString += ("nd")
        elif data[index][self.DATE][self.DATE_DAY] == 3:
            dateString += ("rd")
        elif data[index][self.DATE][self.DATE_DAY] == 23:
            dateString += ("rd")
        else:
            dateString += ("th")
        return dateString
