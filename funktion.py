# Task nr.1: 
# Create a mini program that takes 10 random numbers in
# one input ("1,2,5 76,89 ...etc")Write functions to: calculate their sum, 
# multiplication of highest and lowest numbersand the function
# which makes a new string where numbers are positioned from highest to lowest.



# from typing import List


# def find_sum(number_list: List[int]) -> int:
#     return sum(number_list)
# numbers_input = input("Please enter 10 random numbers: ")
# number_list = [int(number) for number in numbers_input.split(",")]

# result = find_sum(number_list)
# print("Sum of the numbers:", result)

# def find_multiplication(nuber_list:List[int])->int:
#     return min(number_list) * max(number_list)
# multipication_list = find_multiplication(number_list)
# print("multiplication of highest and lowest number: ", multipication_list)

# def find_sorted(number_list:List[int])->int:
#     return sorted(number_list,reverse=True)
# sorted_list = find_sorted(number_list)
# print ("from highest to lowest nuber: ",sorted_list)

# be funkcijos pvz:

# max_number = max(number_list)
# min_number = min(number_list)
# print("multiplication of highest and lowest number:",max_number * min_number)

# sorted_num = sorted(number_list,reverse=True)
# print("from highest to lowest nuber: ", sorted_num )

# User enters two names separated by comma : for example :('Mindaugas PiktasDestytojas, Mindaugas Juokauja')
# Create a function that would swipe surnames and will prduxe new name surname and
# another function funtion that will swap names.


# def swap_surnames(names_and_surname: str) -> str:
#     name_and_surname1, name_and_surname2 = names_and_surname.split(', ')

#     name1, surname1 = name_and_surname1.split(' ')
#     name2, surname2 = name_and_surname2.split(' ')

#     new_name1 = f'{name1} {surname2}'
#     new_name2 = f'{name2} {surname1}'
    
#     return f'({new_name1}, {new_name2})'

# user_input = input("Enter two names and surnames separated by comma: ")
# result = swap_surnames(user_input)
# print("Swapped surname:", result)

# def swap_names(names_and_surname):
#     name_and_surname1, name_and_surname2 = names_and_surname.split(', ')

#     name1, surname1 = name_and_surname1.split(' ')
#     name2, surname2 = name_and_surname2.split(' ')

#     new_name1 = f'{name2} {surname1}'
#     new_name2 = f'{name1} {surname2}'
    
#     return f'({new_name1}, {new_name2})'

# user_input = input("Enter two names and surnames separated by comma: ")
# result = swap_names(user_input)
# print("Swapped names:", result)



# def convert_to_celsius(temp_f: float=75) -> float:
#     return (temp_f - 32) *5 / 9 

# print(f"room temperature:{round(convert_to_celsius(), 1)} C")

# def print_leter(letter: str, *args, **kwargs) -> str:
#     print(letter)
#     if args:
#         print( f"Args:{args}")
#     if kwargs:
#         print(f"Kwargs:{kwargs}")
#     return letter
# print_leter("A", 25, 32, name = "Antanas")

# def sum_two_number(no_a: int,no_b: int=10)->int:
#     return no_a+no_b
# print(f"sum of number: {sum_two_number(5)}")

# def multi_two_number(no_a: int,no_b: int)->int:
#     return no_a * no_b
# print(f"sum of number: {multi_two_number(5,5)}")

# multiplication = lambda a, b: a * b
# print(multiplication(5,5))

# add_default_quantity = lambda amount: amount + 25
# print(add_default_quantity(444))

# 1) Create a function which converts lenght, mass, time units from SI system to CGS. All arguments must hold 
# default values if not provided.

# 1) Sukurkite funkciją, kuri konvertuoja ilgį, masę, laiko vienetus iš SI sistemos į CGS. Visi argumentai turi būti 
# numatytosios vertės, jei nepateiktos.

# def si_convert_to_cgs(length_m: float = 1.0, mass_kg: float =1.0, time_min: float =1.0) -> str:
#     return f" Lenght in CGS: {round(length_m * 100)} cm,\n Mass in cgs: {round(mass_kg * 1000)} g,\n Time in CGS: {round(time_min * 60)} s."
# rezult = si_convert_to_cgs (6, 2, 2)

# print(rezult)
   


# 2) Create a program which takes 5 random number per 1 input.The create a function which takes the sum of 
# those numbers (lets agree argument is being called 'num_sum'),and all those 5 numbers as separate free arguments 
# as well.Multiply all those numbers with with the num_sum you calculated in a list data structure.

# Sukurkite programą, kuri užima 5 atsitiktinius skaičius 1 įvestyje. Sukurti funkciją, kuri užima 
# tie skaičiai (tarkime, argumentas vadinamas "num_sum"),ir visi tie 5 skaičiai kaip atskiri laisvi argumentai 
# taip pat. Padauginkite visus šiuos skaičius iš num_sum, kurį apskaičiavote sąrašo duomenų struktūroje.

from typing import List


def find_sum(number_list: List[int]) -> int:
    return sum(number_list)
numbers_input = input("Please enter 5 random numbers: ")
number_list = [int(number) for number in numbers_input.split(",")]
num_sum: int = sum (number_list)

print ("sum of numbers: ", num_sum)
num_multiplication: list = [i * num_sum for i in number_list ]
print ("multiplication of number: ",num_multiplication)





# 3) Create lamba functions for these caclulations: - calculate circle radius - calculate average speed of the car 
# (knowing distance and time passed to drive that distance) - calculate percentage ofvalue if 5500 is equal 200%

