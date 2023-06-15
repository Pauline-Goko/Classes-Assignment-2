# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
  
from fnmatch import translate


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
        print(f"{self.name} is telling a {story.title} story which is a  {self.language} story to {self.age_group} children")

class Translator:
    def __init__(self, name, original_language, translated_language):
        self.name = name
        self.original_language = original_language
        self.translated_language = translated_language
    
    def translate(self, story):
    
        translated_content = translate(story.content)
        
        translated_story = Story(
            title = story.title,
            content = translated_content,
            length = story.length,
            moral_lessons = story.moral_lessons,
            age_group = story.age_group
        )
        
        return translated_story

# Create an instance of Story
story1 = Story(
    "Mwangi, the brave boy","A boy that went searching for his beloved dog in the deadly forest","20 pages", "Bravery and courage", "5-10 years")

# Create an instance of StoryTeller
storyteller1 = StoryTeller("Kamau Maina", "Kikuyu", "5-10 years")

# Tell the story
storyteller1.tell_story(story1)

# Create an instance of Translator
translator1 = Translator("Translator1", "Kikuyu", "English")

# Translate the story
translated_story = translator1.translate(story1)

# Output the translated story
print(f"Translated story: {translated_story.title}: {translated_story.content}")


# Create an instance of Story2
story2 = Story("Jamba Nene", "a boy that met an ogre in the deadly forest", "40 pages", "obedience", "11-15 years")

# Create an instance of StoryTeller
storyteller2 = StoryTeller("Wambui Muriithi", "Kikuyu", "11-15 years")

# Tell the story
storyteller2.tell_story(story2)

# Create an instance of Translator
translator2 = Translator("Translator2", "Kikuyu", "English")

# Translate the story
translated_story = translator2.translate(story2)

# Output the translated story
print(f"Translated Story: {translated_story.title}: {translated_story.content}")


# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.



# Recipe class
class Recipe:
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    self.name = name
    self.ingredients = ingredients
    self.preparation_time = preparation_time
    self.cooking_method = cooking_method
    self.nutritional_info = nutritional_info

  # Method to display the recipe details
  def display_recipe(self):
    print(f"Recipe: {self.name}")
    print(f"Ingredients: {self.ingredients}")
    print(f"Preparation Time: {self.preparation_time}")
    print(f"Cooking Method: {self.cooking_method}")
    print(f"Nutritional Information: {self.nutritional_info}")

# Subclass for Moroccan recipes
class MoroccanRecipe(Recipe):
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
   

  # Method to display additional Moroccan recipe details
  def display_moroccan_recipe(self):
    print()

# Subclass for Ethiopian recipes
class EthiopianRecipe(Recipe):
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
 

  # Method to display additional Ethiopian recipe details
  def display_ethiopian_recipe(self):
    print()

# Subclass for Nigerian recipes
class NigerianRecipe(Recipe):
  def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
    super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
   

  # Method to display additional Nigerian recipe details
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

