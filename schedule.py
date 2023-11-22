"""schedule"""

"""To do: list of days, dictionary of employee id and desired days scheduled / days desired / name, actual"""


import day
import employee


class Schedule:
    """Represents a generic controller with 4 buttons."""

    def __init__(self, day_list: list[day.Day] = [],
                 employee_list: list[employee.Employee] = []):
                 #scheduled_employee_dict: dict[int, list] = {employee.Employee.id: [1,2,3,4,5,6,7], employee.Employee.id: 0}):
        """Initializes 4 buttons. w, a, s, and d."""

        self.day_list = day_list
        self.employee_list = employee_list
        #self.scheduled_employee_dict = scheduled_employee_dict

    def generate(self):
        # put a perosn in a random day, see if it works, if not, try another day. if it never works with them try another person. if it never works say schedule is not possible
        self.day_list[0].name
        self.employee_list[0].days_available[0]

        print(self.employee_list[0].days_available[0])

    def check_day_ids(self):
        """checks that each day id is unique"""

        id_list = []
        
        for element in self.day_list:
            id_list.append(element.id)
        
        id_list.sort()# change to personal function
        
        test = 0
 
        test = len(set(id_list)) == len(id_list)
        
        if(test):
            pass
        else:
            raise TypeError # change

    def sort_days(self):
        #recursive sort by id
        pass

    def check_employee_ids(self):
        """checks that each day id is unique"""

        id_list = []
        
        for element in self.employee_list:
            id_list.append(element.id)
        
        id_list.sort()# change to personal function
        
        test = 0
 
        test = len(set(id_list)) == len(id_list)
        
        if(test):
            pass
        else:
            raise TypeError # change

