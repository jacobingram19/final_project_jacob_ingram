""""employee"""

"""To do: id, Name, days of the week available, desired number of days"""


class Employee:
    """Represents a generic controller with 4 buttons."""

    def __init__(self, id=0,
                 name="unknown",
                 days_available: list[int] = [1,2,3,4,5,6,7], 
                 target_days=0):
        """Initializes 4 buttons. w, a, s, and d."""

        self.id = id
        self.name = name

        if len(days_available) < 8:
            self.days_available = days_available
        else:
            print("Employees cannot be available more than 7 days a week.")

        if target_days < 8:
            self.target_days = target_days
        else:
            print("Employees cannot be work more than 7 days a week.")

    #def sort days_available also make sure they are 1 through 7