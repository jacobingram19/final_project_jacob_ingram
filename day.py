"""day of the week"""

"""To do: id, name, number of people needed, list of people"""


import employee


class Day:
    """Represents a generic controller with 4 buttons."""

    def __init__(self, id=1,
                 name="unknown",
                 employees_needed = 0, 
                 employees: list[employee.Employee] = []):
        """Initializes 4 buttons. w, a, s, and d."""

        self.id = id # make sure that these are 1 through 7
        self.name = name
        self.employees_needed = employees_needed

        if len(employees) <= employees_needed:
            self.employees = employees
        else:
            print("There cannot be more employees than are needed.")