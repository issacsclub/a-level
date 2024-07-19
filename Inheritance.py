class employee:
     def __init__ (self, name, staffno):
         self.name = name
         self.__staffno = staffno 
         self.__fullTimeStaff = True
       
         
     def showDetails(self):
         print("Employee Name " + self.name)
         print("Employee Number " , self.__staffno)
         
class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno) 
        self.__fullTimeStaff = False
        self.__hoursWorked = 0
    def getHoursWorked (self):
        return(self.__hoursWorked)

class fullTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = True
        self.__yearlySalary = 0
    def getYearlySalary (self):
        return(self.__yearlySalary)
    
permanentStaff = fullTime("Eric Jones", 72)
permanentStaff.showDetails()
temporaryStaff = partTime ("Alice Hue", 1017)
temporaryStaff.showDetails ()
