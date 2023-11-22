"""main"""


import schedule
import day
import employee


def main():

    day_1 = day.Day(1,"Sunday",2)
    day_2 = day.Day(2,"Monday",2)
    day_3 = day.Day(3,"Tuesday",2)
    day_4 = day.Day(4,"Wednesday",2)
    day_5 = day.Day(5,"Thursday",2)
    day_6 = day.Day(6,"Friday",2)
    day_7 = day.Day(7,"Saturday",2)

    day_list = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]

    employee_1 = employee.Employee(1, "Aaron", [1,6,7], 2)
    employee_2 = employee.Employee(2, "Brett", [2,3,4,5,6], 5)
    employee_3 = employee.Employee(3, "Cameron", [1,2,3,4,5,6,7], 7)

    employee_list = [employee_1, employee_2, employee_3]

    schedule_1 = schedule.Schedule(day_list, employee_list)

    schedule_1.check_day_ids()
    schedule_1.check_employee_ids()
    schedule_1.generate()
    
if __name__ == "__main__":
    main()