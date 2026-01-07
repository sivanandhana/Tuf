"""
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid

"""
class Solution:
    def whichWeekDay(self, day):
        if day == 1:
            print("Monday")

        elif day == 2:
            print("Tuesday")

        elif day == 3:
            print("Wednesday")

        elif day == 4:
            print("Thursday")

        elif day == 5:
            print("Friday")

        elif day == 6:
            print("Saturday")

        elif day == 7:
            print("Sunday")

        else:
            print("Invalid")
solution_instance = Solution()
solution_instance.whichWeekDay(5)