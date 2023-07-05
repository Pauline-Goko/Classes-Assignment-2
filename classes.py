# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
  
class Story:
    def __init__(self, title, content, length, moral_lessons, age_group):
      self.title = title
      self.content = content
      self.length = length
      self.moral_lessons = moral_lessons
      self.age_group = age_group


class StoryTeller:
    def __init__(self, name, language, age_group):
      self.name = name
      self.language = language
      self.age_group = age_group

    def tell_story(self, story):
        print(
            f"{self.name} is telling a {story.title} story which is a {self.language} story to {story.age_group} children. It is {story.length} long, and the moral lessons are {story.moral_lessons}.")


class Translator:
    def __init__(self, name, original_language, translated_language):
      self.name = name
      self.original_language = original_language
      self.translated_language = translated_language

    def translate_content(self, content):
     return content


story1 = Story("Mwangi, the brave boy", "A boy that went searching for his beloved dog in the deadly forest",
               "20 pages", "bravery and courage", "5-10 years")

storyteller1 = StoryTeller("Kamau Maina", "Kikuyu", "5-10 years")
storyteller1.tell_story(story1)

translator1 = Translator("Pauline", "Kikuyu", "English")
print(f"The translator {translator1.name} is translating {story1.title} story from {translator1.original_language} to {translator1.translated_language}")

story2 = Story("Jamba Nene", "A boy that met an ogre in the deadly forest", "40 pages", "obedience and courage",
               "11-15 years")

storyteller2 = StoryTeller("Wambui Kamau", "Kikuyu", "11-15 years")
storyteller2.tell_story(story2)

translator = Translator("Lucky", "French", "English")
print(f"The translator {translator.name} is translating the {story2.title} story from {translator.original_language} to {translator.translated_language}")



# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.


class Recipe:
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    self.name = name
    self.ingredients = ingredients
    self.preparation_time = preparation_time
    self.cooking_method = cooking_method
    self.nutritional_info = nutritional_info

 
  def display_recipe(self):
    print(f"Recipe: {self.name}")
    print(f"Ingredients: {self.ingredients}")
    print(f"Preparation Time: {self.preparation_time}")
    print(f"Cooking Method: {self.cooking_method}")
    print(f"Nutritional Information: {self.nutritional_info}")

class MoroccanRecipe(Recipe):
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
   

  def display_moroccan_recipe(self):
    print()

class EthiopianRecipe(Recipe):
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
 

  def display_ethiopian_recipe(self):
    print()


class NigerianRecipe(Recipe):
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
   
  def display_nigerian_recipe(self):
    print()


moroccan_recipe = MoroccanRecipe(
  "Fried Chicken",
  ["Chicken", "Onions", "Spices", "Olives"],
  "2 hours",
  "Frying",
  "Calories: 400, Fat: 15g, Protein: 30g",
 
)

moroccan_recipe.display_recipe()
moroccan_recipe.display_moroccan_recipe()

ethiopian_recipe = EthiopianRecipe(
  "Injera",
  ["Chicken", "Onions", "Spice"],
  "3 hours",
  "Baking",
  "Calories: 450, Fat: 20g, Protein: 25g",

)

ethiopian_recipe.display_recipe()
ethiopian_recipe.display_ethiopian_recipe()

nigerian_recipe = NigerianRecipe(
  "Jollof Rice",
  ["Rice", "Tomatoes", "Onions", "Peppers", "Chicken"],
  "1 hour",
  "Boiling, Frying",
  "Calories: 300, Fat: 8g, Protein: 20g",
 
)

nigerian_recipe.display_recipe()
nigerian_recipe.display_nigerian_recipe()



#**Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
#characteristics and behaviors, such as its diet, typical lifespan, migration
#patterns, etc. Some species might be predators, others prey. You'll need to
#create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
#these classes might relate to each other through inheritance.


# class Species:
#     def __init__(self, name, diet, lifespan, month):
#         self.name = name
#         self.diet = diet
#         self.lifespan = lifespan
#         self.month = month
#     def track(self):
#         if self.month<=0:
#             return 'Invalid month entry'
#         elif self.month<=6:
#             migration_pattern = 'East to West'
#             return f"{self.name}\n Diet:{self.diet}\n Lifespan:{self.lifespan}\n Prey:{self.prey}\n               Migration pattern:{migration_pattern}"
#         elif self.month>=6 and self.month<=12:
#             migration_pattern = 'West to East'
#             return f"{self.name}\n Diet:{self.diet}\n Lifespan:{self.lifespan}\n Migration pattern:{migration_pattern}"
#         return 'Month entry must be in the calendar'
# class Predator(Species):
#     def __init__(self, name, diet, lifespan, month, prey):
#         super().__init__(name, diet, lifespan, month)
#         self.prey = prey
        
#     def track_predator(self):
#         track = super().track()
#         return f"{track}\n Prey:{self.prey}"
# class Prey(Species):
#     def __init__(self, name, diet, lifespan, month, predator):
#         super().__init__(name, diet, lifespan, month)
#         self.predator = predator
#     def track_prey(self):
#         track = super().track()
#         return f"{track}\n Predator:{self.predator}"
# animal_one = Predator('Lion', 'Herbivores', '30yrs', 6, ['Antelopes', 'Gazelles', 'Zebras'])
# print(animal_one.track_predator())

# animal_two = Prey('Zebra', 'Vegetation', '8yrs', 7, ['Cheetah', 'Lion', 'Black Panther'])
# print(animal_two.track_prey())



class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan


class Predator(Species):
    def __init__(self, name, diet, lifespan):
        super().__init__(name, diet, lifespan)


class Prey(Species):
    def __init__(self, name, diet, lifespan, migrationPattern):
        super().__init__(name, diet, lifespan)
        self.migrationPattern = migrationPattern



lion = Predator("Lion", "Carnivore", "15 years")
zebra = Prey("Zebra", "Herbivore", "10 years", "Seasonal migration")
print(lion.__dict__)
print(zebra.__dict__)




     
     
# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.
     
     

# class Artist:
#     def __init__(self, name, country, music_style, instruments):
#         self.name = name
#         self.country = country
#         self.music_style = music_style
#         self.instruments = instruments

#     def introduce(self):
#         print(f"I am {self.name} from {self.country}.")


# class Performance:
#     def __init__(self, artist, start_time, end_time):
#         self.artist = artist
#         self.start_time = start_time
#         self.end_time = end_time

#     def display_info(self):
#         print(f"Performance by {self.artist.name} from {self.artist.country}.")
#         print(f"Start time: {self.start_time}, End time: {self.end_time}")


# class Stage:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.performances = []

#     def add_performance(self, performance):
#         self.performances.append(performance)

#     def display_schedule(self):
#         # print(f"Schedule for Stage {self.name}:")
#         for performance in self.performances:
#             performance.display_info()
#             print()


# class SpecialPerformance(Performance):
#     def __init__(self, artist, start_time, end_time, special_event):
#         super().__init__(artist, start_time, end_time)
#         self.special_event = special_event

#     def display_info(self):
#         super().display_info()
#         print(f"Special Event: {self.special_event}")


# # Example usage
# artist1 = Artist("Rema", "Nigeria", "Afrobeats", "Drum")
# artist2 = Artist("Diamond", "Tanzania", "Bongo", "Guitar")
# artist3 = Artist("Sauti Sol", "Kenya", "Zilipedwa", "Guitar")

# print(artist1.introduce())

# performance1 = Performance(artist1, "18:00", "19:00")
# performance2 = Performance(artist2, "19:30", "20:30")
# performance3 = SpecialPerformance(artist3, "21:00", "22:00", "Fireworks Show")

# stage1 = Stage(500)
# stage1.add_performance(performance1)
# stage1.add_performance(performance2)
# stage1.add_performance(performance3)

# print(stage1.display_schedule())




class Artist:
    def __init__(self, name, country, music_style, instruments):
        self.name = name
        self.country = country
        self.music_style = music_style
        self.instruments = instruments



class Performance:
    def __init__(self, artist, stage_name, capacity, start_time, end_time, ):
        self.artist = artist
        self.stage_name = stage_name
        self.capacity = capacity
        self.start_time = start_time
        self.end_time = end_time

    def display_info(self):
        print(f"Performance by {self.artist.name} from {self.artist.country}.")
        print(f"Music Style: {self.artist.music_style}")
        print(f"Instruments: {self.artist.instruments}")
        print(f"Stage: {self.stage_name}")
        print(f"Capacity: {self.capacity}")
        print(f"Start time: {self.start_time}, End time: {self.end_time}")


artist1 = Artist("Rema", "Nigeria", "Afrobeats", "Drum")
artist2 = Artist("Diamond", "Tanzania", "Bongo", "Guitar")
artist3 = Artist("Sauti Sol", "Kenya", "Zilipendwa", "Guitar")


performance1 = Performance(artist1, "Carnivore","400","18:00", "19:00")
performance2 = Performance(artist2,"Alchemist","250", "19:30", "20:30")
performance3 = Performance(artist3, "Kasarani Stadium","1000","20:30", "10:30")


performance1.display_info()
performance2.display_info()
performance3.display_info()



# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_value(self):
        return self.price * self.quantity


# Create multiple Product objects
product1 = Product("Avocado", 20, 10)
product2 = Product("Melon", 30, 15)
product3 = Product("Pineanpple", 60, 20)

# Calculate total values
total_value1 = product1.calculate_total_value()
total_value2 = product2.calculate_total_value()
total_value3 = product3.calculate_total_value()

# Calculate the overall total value
overall_total_value = total_value1 + total_value2 + total_value3

# Print the results
print(f"Total value of {product1.name}: {total_value1}")
print(f"Total value of {product2.name}: {total_value2}")
print(f"Total value of {product3.name}: {total_value3}")
print(f"Overall total value: {overall_total_value}")



# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60



student1 = Student("Joan Samuel", 18, [85, 90, 76, 92, 88])
student1.display_student_info()
print(f"Average Grade: {student1.calculate_average_grade()}")
print(f"Has Passed: {student1.has_passed()}")

student2 = Student("Janet Kaleche", 20, [45, 15, 10, 70, 80])
student2.display_student_info()
print(f"Average Grade: {student2.calculate_average_grade()}")
print(f"Has Passed: {student2.has_passed()}")



# Create a FlightBooking class that represents a flight booking system. Implement methods to 
# search for available flights based on destination and date, reserve seats for customers, 
# manage passenger information, and generate booking Confirmations.

class FlightBookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight_number, destination, date, available_seats):
        flight = {
            "flight_number": flight_number,
            "destination": destination,
            "date": date,
            "available_seats": available_seats,
            "passengers": []
        }
        self.flights.append(flight)

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if (
                flight["destination"] == destination and
                flight["date"] == date and
                flight["available_seats"] > 0
            ):
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, flight_number, passenger_name):
        flight = next((flight for flight in self.flights if flight["flight_number"] == flight_number), None)
        if flight and flight["available_seats"] > 0:
            flight["available_seats"] -= 1
            flight["passengers"].append(passenger_name)
            return True
        return False

    def get_passenger_info(self, flight_number):
        flight = next((flight for flight in self.flights if flight["flight_number"] == flight_number), None)
        if flight:
            return flight["passengers"]
        return []

    def generate_booking_confirmation(self, flight_number):
        flight = next((flight for flight in self.flights if flight["flight_number"] == flight_number), None)
        if flight:
            passenger_list = "\n".join([f"{index + 1}. {passenger}" for index, passenger in enumerate(flight["passengers"])])
            confirmation = f"Confirmation for Flight {flight['flight_number']}:\n" \
                          f"Destination: {flight['destination']}\n" \
                          f"Date: {flight['date']}\n" \
                          f"Passenger List:\n" \
                          f"{passenger_list}"
            return confirmation
        return "Flight not found"


booking_system = FlightBookingSystem()

booking_system.add_flight("FLY540", "Mombasa", "2023-07-05", 500)
booking_system.add_flight("BOENG560", "London", "2023-07-25", 220)

available_flights = booking_system.search_flights("London", "2023-07-25")
print(available_flights)

flight_number = "BOENG560"
flight_to_reserve = available_flights[0]
passenger_name = "Brigit Amakove"
passenger2 = "Pauline Wanjiru"
seat_reserved = booking_system.reserve_seat(flight_to_reserve["flight_number"], passenger_name)
print(f"Seat reserved for {passenger_name}" if seat_reserved else "No seats available")

seat_reserve = booking_system.reserve_seat(flight_to_reserve["flight_number"], passenger2)
print(f"Seat reserved for {passenger2}" if seat_reserve else "No seats available")

passengers_info = booking_system.get_passenger_info(flight_to_reserve["flight_number"])
print(f"Passenger information for {flight_to_reserve['flight_number']}: {passengers_info}")

confirmation = booking_system.generate_booking_confirmation(flight_to_reserve["flight_number"])
print(confirmation)


# Create a LibraryCatalog class that handles the cataloging and management of books in a library.
# Implement methods to add new books, search for books by title or author, keep track of available copies, 
# and display book details. 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies, year):
        book = {
            "title": title,
            "author": author,
            "copies": copies,
            "year": year
        }
        self.books.append(book)

    def search_book(self, title):
        found_books = [book for book in self.books if book["title"].lower() == title.lower()]
        return found_books

    def display_books(self):
        if not self.books:
            print("No books found.")
        else:
            for book in self.books:
                print(f"{book['title']} by {book['author']}, Year: {book['year']}, Copies: {book['copies']}")


library = Library()
library.add_book("Born a Crime", "Trevor Noah", 300, 2019)
library.add_book("Originals", "Adam Grant", 22, 2017)
library.add_book("The Kite Runner", "Hussein Mohammed", 18, 2009)

found_books = library.search_book("Originals")
print(found_books)

library.display_books()
