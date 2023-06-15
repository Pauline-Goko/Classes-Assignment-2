// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.


class Story {
    constructor(title, content, length, moral_lessons, age_group) {
      this.title = title;
      this.content = content;
      this.length = length;
      this.moral_lessons = moral_lessons;
      this.age_group = age_group;
    }
  }
  
  class StoryTeller {
    constructor(name, language, age_group) {
      this.name = name;
      this.language = language;
      this.age_group = age_group;
    }
  
    tell_story(story) {
      console.log(`${this.name} is telling a ${story.title} story which is a ${this.language} story to ${this.age_group} children`);
    }
  }
  
  class Translator {
    constructor(name, original_language, translated_language) {
      this.name = name;
      this.original_language = original_language;
      this.translated_language = translated_language;
    }
  
  
    translate(story) {
      const translated_content = translate(story.content);
  
      const translated_story = new Story(
        story.title,
        translated_content,
        story.length,
        story.moral_lessons,
        story.age_group
      );
  
      return translated_story;
    }
  }
  
  // Created an instance of Story
  const story1 = new Story( "Mwangi, the brave boy", "A boy that went searching for his beloved dog in the deadly forest", "20 pages", "Bravery and courage", "5-10 years");
  
  // Created an instance of StoryTeller
  const storyteller1 = new StoryTeller("Kamau Maina", "Kikuyu", "5-10 years");
  
  // Tell the story
  storyteller1.tell_story(story1);
  
  // Created an instance of Translator
  const translator1 = new Translator("Translator1", "Kikuyu", "English");
  
  // Translate the story
  const translated_story1 = translator1.translate(story1);
  
  // Output the translated story
  console.log(`Translated story: ${translated_story1.title}: ${translated_story.content}`);
  
  // Created an instance of Story2
  const story2 = new Story( "Jamba Nene", "a boy that met an ogre in the deadly forest", "40 pages", "obedience", "11-15 years" );
  
  // Create an instance of StoryTeller
  const storyteller2 = new StoryTeller("Wambui Kamau", "Kikuyu", "11-15 years");
  
  // Tell the story
  storyteller2.tell_story(story2);
  
  // Created an instance of Translator
  const translator2 = new Translator("Translator2", "Kikuyu", "English");
  
  // Translate the story
  const translated_story2 = translator2.translate(story2);
  
  // Output the translated story
  console.log(`Translated Story: ${translated_story2.title}: ${translated_story2.content}`);
  



//   **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.


// Recipe class
class Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    this.name = name;
    this.ingredients = ingredients;
    this.preparationTime = preparationTime;
    this.cookingMethod = cookingMethod;
    this.nutritionalInfo = nutritionalInfo;
  }

  // Method to display the recipe details
  displayRecipe() {
    console.log(`Recipe: ${this.name}`);
    console.log(`Ingredients: ${this.ingredients}`);
    console.log(`Preparation Time: ${this.preparationTime}`);
    console.log(`Cooking Method: ${this.cookingMethod}`);
    console.log(`Nutritional Information: ${this.nutritionalInfo}`);
  }
}

// Subclass for Moroccan recipes
class MoroccanRecipe extends Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    super(name, ingredients, preparationTime, cookingMethod, nutritionalInfo);
    
  }

  // Method to display Moroccan recipe details
  displayMoroccanRecipe() {
    console.log();
  }
}

// Subclass for Ethiopian recipes
class EthiopianRecipe extends Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    super(name, ingredients, preparationTime, cookingMethod, nutritionalInfo);
    
  }

  // Method to display  Ethiopian recipe details
  displayEthiopianRecipe() {
    console.log();
  }
}

// Subclass for Nigerian recipes
class NigerianRecipe extends Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo,) {
    super(name, ingredients, preparationTime, cookingMethod, nutritionalInfo);
    
  }

  // Method to display Nigerian recipe details
  displayNigerianRecipe() {
    console.log();
  }
}


const moroccanRecipe = new MoroccanRecipe(
  "Fried Chicken",
  ["Chicken", "Onions", "Spices", "Olives"],
  "2 hours",
  "Simmering",
  "Calories: 400, Fat: 15g, Protein: 30g",
 
);

moroccanRecipe.displayRecipe();
moroccanRecipe.displayMoroccanRecipe();

const ethiopianRecipe = new EthiopianRecipe(
  "Injera",
  ["Chicken", "Onions", "spices"],
  "3 hours",
  "Stewing",
  "Calories: 450, Fat: 20g, Protein: 25g",
 
);

ethiopianRecipe.displayRecipe();
ethiopianRecipe.displayEthiopianRecipe();

const nigerianRecipe = new NigerianRecipe(
  "Jollof Rice",
  ["Rice", "Tomatoes", "Onions", "Peppers", "Chicken"],
  "1 hour",
  "Boiling, Frying",
  "Calories: 300, Fat: 8g, Protein: 20g",
 
);

nigerianRecipe.displayRecipe();
nigerianRecipe.displayNigerianRecipe();


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.



// Species class
class Species {
  constructor(name, diet, lifespan) {
    this.name = name;
    this.diet = diet;
    this.lifespan = lifespan;
  }
}

// Predator class (inherits from Species)
class Predator extends Species {
  constructor(name, diet, lifespan, huntingMethod) {
    super(name, diet, lifespan);
    this.huntingMethod = huntingMethod;
  }
}

// Prey class (inherits from Species)
class Prey extends Species {
  constructor(name, diet, lifespan, migrationPattern) {
    super(name, diet, lifespan);
    this.migrationPattern = migrationPattern;
  }
}


const lion = new Predator("Lion", "Carnivore", 15, "Stalking");
const zebra = new Prey("Zebra", "Herbivore", 10, "Seasonal migration");
