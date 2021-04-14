import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid

# Create a dictionary for the data | characters [Importance, weights]
characters = {
    'Regulus Arcturus Black': [15, 10],
    'Sirius Black': [70, 8],
    'Lavender Brown': [40, 3],
    'Cho Chang': [50, 6],
    'Vincent Crabbe Sr.': [10, 9],
    'Vincent Crabbe': [25, 9],
    'Bartemius "Barty" Crouch Sr.': [15, 11],
    'Bartemius "Barty" Crouch Jr.': [15, 7],
    'Fleur Delacour': [60, 7],
    'Cedric Diggory': [50, 6],
    'Alberforth Dumbledore': [30, 30],
    'Albus Dumbledore': [100, 30],
    'Dudley Dursley': [50, 30],
    'Petunia Dursley': [50, 30],
    'Vernon Dursley': [50, 26],
    'Argus Filch': [40, 19],
    'Seamus Finnigan': [40, 22],
    'Nicolas Flamel': [10, 1],
    'Cornelius Fudge': [60, 1],
    'Goyle Sr.': [10, 10],
    'Gregory Goyle': [30, 8],
    'Hermione Granger': [100, 3],
    'Rubeus Hagrid': [100, 6],
    'Igor Karkaroff': [20, 9],
    'Viktor Krum': [25, 9],
    'Bellatrix Lestrange': [70, 11],
    'Alice Longbottom': [10, 7],
    'Frank Longbottom': [10, 7],
    'Neville Longbottom': [90, 6],
    'Luna Lovegood': [70, 30],
    'Xenophilius Lovegood': [70, 30],
    'Remus Lupin': [90, 30],
    'Draco Malfoy': [100, 30],
    'Lucius Malfoy': [70, 26],
    'Narcissa Malfoy': [40, 19],
    'Olympe Maxime': [30, 22],
    'Minerva McGonagall': [90, 1],
    'Alastor "Mad-Eye" Moody': [70, 1],
    'Peter Pettigrew': [70, 10],
    'Harry Potter': [100, 8],
    'James Potter': [25, 3],
    'Lily Potter': [25, 6],
    'Quirinus Quirrell': [30, 9],
    'Tom Riddle Sr.': [10, 9],
    'Mary Riddle': [10, 11],
    'Lord Voldemort': [100, 7],
    'Rita Skeeter': [20, 7],
    'Severus Snape': [100, 6],
    'Nymphadora Tonks': [70, 30],
    'Dolores Janes Umbridge': [30, 30],
    'Arthur Weasley': [85, 30],
    'Bill Weasley': [60, 30],
    'Charlie Weasley': [65, 26],
    'Fred Weasley': [95, 19],
    'George Weasley': [95, 22],
    'Ginny Weasley': [95, 1],
    'Molly Weasley': [85, 1],
    'Percy Weasley': [65, 10],
    'Ron Weasley': [100, 8],
    'Dobby': [85, 3],
    'Fluffy': [20, 6],
    'Hedwig': [100, 9],
    'Moaning Myrtle': [30, 9],
    'Aragog': [25, 11],
    'Grawp': [10, 7]
}

# Create the columns name
columns = ['ID', 'Character', 'Importance', 'House', 'Living']

def generate_random_house_and_place():
  houses = ['Gryffindor', 'Slytherin', 'Raveclaw', 'Hufflepuff']
  places = ['Hogwarts', 'Hogsmead', 'Godric Hollows', 'Others']
  weights = [1,2,3,4]

  # Random house got choose
  houses = random.choice(houses)
  # Index
  index = random.choices(range(len(places)), weights=weights)[0]

  return f"{houses}, {places[index]}"

# Function to write the rows for the mock data
def write_row(order_number, character, house, living):
  importance = characters[character][0]
  output = [order_number, character, importance, house, living]
  return output

if __name__ == '__main__':
  order_number = 1
  orders_amount = int(numpy.random.normal(loc=40, scale=20)) # numpy.random.normal -> Create an interval of Mock Data with a scaling of possible data

  character_list = [character for character in characters]
  weights = [characters[character][1] for character in characters]

  df = pd.DataFrame(columns=columns)
  print(orders_amount)

  i = 0
  while orders_amount > 0:

    living = generate_random_house_and_place()
    house = None

    character_choice = random.choices(character_list, weights)[0]
    df.loc[i] = write_row(order_number, character_choice, house, living)
    i += 1

    # Add some characters to orders with selected characters
    if character_choice == 'Harry Potter':
      if random.random() < 0.85:
        df.loc[i] = write_row(order_number, "Ron Weasley", house, living)
        i += 1
      if random.random() < 0.85:
        df.loc[i] = write_row(order_number, "Hermione Granger", house, living)
        i += 1
      if random.random() < 0.90:
        df.loc[i] = write_row(order_number, "Hedwig", house, living)
        i += 1

    elif character_choice == "Lord Voldemort":
      if random.random() < 0.90:
        df.loc[i] = write_row(order_number, "Bellatrix Lestrange", house, living)
        i += 1
      if random.random() < 0.85:
        df.loc[i] = write_row(order_number, "Tom Riddle Sr.", house, living)
        i += 1
      if random.random() < 0.70:
        df.loc[i] = write_row(order_number, "Severus Snape", house, living)
        i += 1

    order_number += 1
    orders_amount -= 1

  df.to_csv('./tmp/'f"Mock_Data.csv", index=False)
