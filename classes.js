// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.

class Story {
  constructor(title, content, length, moralLessons, ageGroup) {
    this.title = title;
    this.content = content;
    this.length = length;
    this.moralLessons = moralLessons;
    this.ageGroup = ageGroup;
  }
}

class StoryTeller {
  constructor(name, language, ageGroup) {
    this.name = name;
    this.language = language;
    this.ageGroup = ageGroup;
  }

  tellStory(story) {
    console.log(`${this.name} is telling a ${story.title} story which is a ${this.language} story to ${story.ageGroup} children. It is ${story.length} long, and the moral lessons are ${story.moralLessons}.`);
  }
}

class Translator {
  constructor(name, originalLanguage, translatedLanguage) {
    this.name = name;
    this.originalLanguage = originalLanguage;
    this.translatedLanguage = translatedLanguage;
  }

  translateContent(content) {
    return content;
  }
}

const story1 = new Story("Mwangi, the brave boy", "A boy that went searching for his beloved dog in the deadly forest", "20 pages", "bravery and courage", "5-10 years");

const storyteller1 = new StoryTeller("Kamau Maina", "Kikuyu", "5-10 years");
storyteller1.tellStory(story1);

const translator1 = new Translator("Pauline", "Kikuyu", "English");
console.log(`The translator ${translator1.name} is translating ${story1.title} story from ${translator1.originalLanguage} to ${translator1.translatedLanguage}`);

const story2 = new Story("Jamba Nene", "A boy that met an ogre in the deadly forest", "40 pages", "obedience and courage", "11-15 years");

const storyteller2 = new StoryTeller("Wambui Kamau", "Kikuyu", "11-15 years");
storyteller2.tellStory(story2);

const translator2 = new Translator("Lucky", "French", "English");
console.log(`The translator ${translator2.name} is translating the ${story2.title} story from ${translator2.originalLanguage} to ${translator2.translatedLanguage}`);

 
  

//   **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.



class Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    this.name = name;
    this.ingredients = ingredients;
    this.preparationTime = preparationTime;
    this.cookingMethod = cookingMethod;
    this.nutritionalInfo = nutritionalInfo;
  }


  displayRecipe() {
    console.log(`Recipe: ${this.name}`);
    console.log(`Ingredients: ${this.ingredients}`);
    console.log(`Preparation Time: ${this.preparationTime}`);
    console.log(`Cooking Method: ${this.cookingMethod}`);
    console.log(`Nutritional Information: ${this.nutritionalInfo}`);
  }
}

class MoroccanRecipe extends Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    super(name, ingredients, preparationTime, cookingMethod, nutritionalInfo);
    
  }

  displayMoroccanRecipe() {
    console.log();
  }
}

class EthiopianRecipe extends Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
    super(name, ingredients, preparationTime, cookingMethod, nutritionalInfo);
    
  }

  displayEthiopianRecipe() {
    console.log();
  }
}

class NigerianRecipe extends Recipe {
  constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo,) {
    super(name, ingredients, preparationTime, cookingMethod, nutritionalInfo);
    
  }

  displayNigerianRecipe() {
    console.log();
  }
}

const moroccanRecipe = new MoroccanRecipe("Fried Chicken", ["Chicken", "Onions", "Spices", "Olives"],"2 hours","Simmering","Calories: 400, Fat: 15g, Protein: 30g");
moroccanRecipe.displayRecipe();
moroccanRecipe.displayMoroccanRecipe();

const ethiopianRecipe = new EthiopianRecipe( "Injera", ["Chicken", "Onions", "spices"], "3 hours", "Stewing", "Calories: 450, Fat: 20g, Protein: 25g");
ethiopianRecipe.displayRecipe();
ethiopianRecipe.displayEthiopianRecipe();

const nigerianRecipe = new NigerianRecipe("Jollof Rice", ["Rice", "Tomatoes", "Onions", "Peppers", "Chicken"], "1 hour", "Boiling, Frying","Calories: 300, Fat: 8g, Protein: 20g");
nigerianRecipe.displayRecipe();
nigerianRecipe.displayNigerianRecipe();


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.




class Species {
  constructor(name, diet, lifespan) {
    this.name = name;
    this.diet = diet;
    this.lifespan = lifespan;
  }


   }

class Predator extends Species {
  constructor(name, diet, lifespan) {
    super(name, diet, lifespan);
  }
}


class Prey extends Species {
  constructor(name, diet, lifespan, migrationPattern) {
    super(name, diet, lifespan);
    this.migrationPattern = migrationPattern;
  }

  predictMigration(season) {
   if (season === 'wet') {
   return 'No migration will occur.';
   } else if (season === 'dry') {
   return 'Migration will occur.';
   } else {
   return 'Unable to predict migration.';
   }
     }
}


const lion = new Predator("Lion", "Carnivore", "15 years");
const zebra = new Prey("Zebra", "Herbivore", "10 years", "Seasonal migration");
console.log(lion);
console.log(zebra);
console.log(zebra.predictMigration("wet"));





// **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.

class Artist {
  constructor(name, country, musicStyle, instruments) {
    this.name = name;
    this.country = country;
    this.musicStyle = musicStyle;
    this.instruments = instruments;
  }
}

class Performance {
  constructor(artist, stage, startTime, endTime) {
    this.artist = artist;
    this.stage = stage;
    this.startTime = startTime;
    this.endTime = endTime;
  }

  displayInfo() {
    console.log(`Performance by ${this.artist.name} from ${this.artist.country}.`);
    console.log(`Music Style: ${this.artist.musicStyle}`);
    console.log(`Instruments: ${this.artist.instruments}`);
    console.log(`Stage: ${this.stage.stageName}`);
    console.log(`Capacity: ${this.stage.capacity}`);
    console.log(`Start time: ${this.startTime}, End time: ${this.endTime}`);
  }
}

class Stage {
  constructor(stageName, capacity) {
    this.stageName = stageName;
    this.capacity = capacity;
  }
}

const artist1 = new Artist("Rema", "Nigeria", "Afrobeats", "Drum");
const artist2 = new Artist("Diamond", "Tanzania", "Bongo", "Guitar");
const artist3 = new Artist("Sauti Sol", "Kenya", "Zilipendwa", "Guitar");

const stage1 = new Stage("Carnivore", 400);
const stage2 = new Stage("Alchemist", 250);
const stage3 = new Stage("Kasarani Stadium", 1000);

const performance1 = new Performance(artist1, stage1, "18:00", "19:00");
const performance2 = new Performance(artist2, stage2, "19:30", "20:30");
const performance3 = new Performance(artist3, stage3, "20:30", "10:30");

performance1.displayInfo();
performance2.displayInfo();
performance3.displayInfo();


// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class Product {
  constructor(name, price, quantity) {
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }
   calculateTotalValue() {
    return this.price * this.quantity;
  }
}
const product1 = new Product("Smart Tv", 23000, 55);
const product2 = new Product("Fridge", 150000, 34);
const product3 = new Product("Cooker", 550000, 22);


const totalValue1 = product1.calculateTotalValue();
const totalValue2 = product2.calculateTotalValue();
const totalValue3 = product3.calculateTotalValue();


 console.log("Total value of Product 1:", totalValue1);
console.log("Total value of Product 2:", totalValue2);
console.log("Total value of Product 3:", totalValue3);




// Implement a class called Student with attributes for name, age, and grades (a list of integers). 
// Include methods to calculate the average grade, display the student information, and determine if the
// student has passed (average grade >= 60). Create objects for the Student class and demonstrate the usage of these methods.



class Student {
  constructor(name, age, grades) {
      this.name = name;
      this.age = age;
      this.grades = grades;
  }

  calculateAverageGrade() {
      if (this.grades.length === 0) {
          return 0;
      }
      return this.grades.reduce((sum, grade) => sum + grade, 0) / this.grades.length;
  }

  displayStudentInfo() {
      console.log(`Name: ${this.name}`);
      console.log(`Age: ${this.age}`);
      console.log(`Grades: ${this.grades}`);
  }

  hasPassed() {
      const averageGrade = this.calculateAverageGrade();
      return averageGrade >= 60;
  }
}


const student1 = new Student("Emma Mwaniki", 18, [85, 90, 76, 92, 88]);
student1.displayStudentInfo();
console.log(`Average Grade: ${student1.calculateAverageGrade()}`);
console.log(`Has Passed: ${student1.hasPassed()}`);

const student2 = new Student("Mercy Mutheu", 20, [45, 55, 60, 70, 80]);
student2.displayStudentInfo();
console.log(`Average Grade: ${student2.calculateAverageGrade()}`);
console.log(`Has Passed: ${student2.hasPassed()}`);



// Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.

class FlightBookingSystem {
  constructor() {
    this.flights = [];
  }

  addFlight(flightNumber, destination, date, availableSeats) {
    const flight = {
      flightNumber,
      destination,
      date,
      availableSeats,
      passengers: []
    };
    this.flights.push(flight);
  }

  searchFlights(destination, date) {
    const availableFlights = [];
    for (const flight of this.flights) {
      if (
        flight.destination === destination &&
        flight.date === date &&
        flight.availableSeats > 0
      ) {
        availableFlights.push(flight);
      }
    }
    return availableFlights;
  }

  reserveSeat(flightNumber, passengerName) {
    const flight = this.flights.find(flight => flight.flightNumber === flightNumber);
    if (flight && flight.availableSeats > 0) {
      flight.availableSeats -= 1;
      flight.passengers.push(passengerName);
      return true;
    }
    return false;
  }

  getPassengerInfo(flightNumber) {
    const flight = this.flights.find(flight => flight.flightNumber === flightNumber);
    if (flight) {
      return flight.passengers;
    }
    return [];
  }

  generateBookingConfirmation(flightNumber) {
    const flight = this.flights.find(flight => flight.flightNumber === flightNumber);
    if (flight) {
      let passengerList = '';
      flight.passengers.forEach((passenger, index) => {
        passengerList += `${index + 1}. ${passenger}\n`;
      });

      const confirmation = `Confirmation for Flight ${flight.flightNumber}:
      Destination: ${flight.destination}
      Date: ${flight.date}
      Passenger List:
      ${passengerList}`;

      return confirmation;
    }
    return 'Flight not found';
  }
}

const bookingSystem = new FlightBookingSystem();

bookingSystem.addFlight("FLY540", "Mombasa", "2023-07-05", 500);
bookingSystem.addFlight("BOENG560", "London", "2023-07-25", 220);

const availableFlights = bookingSystem.searchFlights("London", "2023-07-25");
console.log(availableFlights);

const flightNumber = "BOENG560";
const flightToReserve = availableFlights[0];
const passengerName = "Brigit Amakove";
const passenger2 = "Pauline Wanjiru"
const seatReserved = bookingSystem.reserveSeat(flightToReserve.flightNumber, passengerName);
console.log(seatReserved ? `Seat reserved for ${passengerName}` : "No seats available");

const seatReserve = bookingSystem.reserveSeat(flightToReserve.flightNumber, passenger2);
console.log(seatReserve ? `Seat reserved for ${passenger2}` : "No seats available");

const passengersInfo = bookingSystem.getPassengerInfo(flightToReserve.flightNumber);
console.log(`Passenger information for ${flightToReserve.flightNumber}: ${passengersInfo}`);

const confirmation = bookingSystem.generateBookingConfirmation(flightToReserve.flightNumber);
console.log(confirmation);


// Create a LibraryCatalog class that handles the cataloging and management of books in a library. 
// Implement methods to add new books, search for books by title or author, 
// keep track of available copies, and display book details


class Library {
  constructor() {
    this.books = [];
  }

  addBook(title, author, copies, year) {
    const book = { title, author, copies, year }; 

    this.books.push(book);
  }

  searchBook(title) {
    const foundBooks = this.books.filter((book) => book.title.toLowerCase() === title.toLowerCase());
    return foundBooks;
  }

  displayBooks() {
    if (this.books.length === 0) {
      console.log("No books found.");
    } else {
      this.books.forEach((book) => {
        console.log(`${book.title} by ${book.author}, Year: ${book.year}, Copies: ${book.copies}`);
      });
    }
  }
}


const library = new Library();
library.addBook("Born a Crime", "Trevor Noah", 300, 2019);
library.addBook("Originals", "Adam Grant", 22, 2017);
library.addBook("The Kite Runner", "Hussein Mohammed", 18, 2009);


const foundBooks = library.searchBook("Originals");
console.log(foundBooks);

library.displayBooks();
