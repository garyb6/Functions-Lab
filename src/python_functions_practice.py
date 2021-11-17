def return_10(): 
    return 10 



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(p1, p2):
    return p1 // p2 #returns whole number. if single, would potentially become a float

def length_of_string (string):
    return len(string)

def join_string (string1, string2):
    return string1 + string2 

def add_string_as_number(string1, string2):
    return int (string1) + int (string2)

def number_to_full_month_name (month_num):
    if month_num == 1:
        return "January"
    elif month_num == 2:
        return "February"
    elif month_num == 3:
        return "March"
    elif month_num == 4:
        return "April"
    elif month_num == 5:
        return "May"
    elif month_num == 6:
        return "June"
    elif month_num == 7:
        return "July"
    elif month_num == 8:
        return "August"
    elif month_num == 9:
        return "September"
    elif month_num == 10:
        return "October"
    elif month_num == 11:
        return "November"
    elif month_num == 12:
        return "December"

print(number_to_full_month_name (11))

#create one function for next 3 def number_to_full_month_name (s1):
#extension - cube - **3 means to the power of 3