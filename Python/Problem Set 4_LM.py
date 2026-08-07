###Problem 1###

# reports = [
#     "SANTOS | Private | Fitness:91 | Status:available",
#     "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
#     "OKAFOR | Sergeant | Fitness:88 | Status:available",
#     "BRIGGS | Private | Fitness:55 | Status:available",
#     "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
#     "REYES | Sergeant | Fitness:79 | Status:available",
# ]
# class Soldier:
#     def __init__(self, name, rank, fitness, deployed):
#         self.name = name
#         self.rank = rank
#         self.fitness = fitness
#         self.deployed = deployed

#     def dispatch(self):
#         self.deployed = True

#     def __str__(self):
#         return (
#             f"{self.name} "
#             f"({self.rank}, fitness: {self.fitness}, "
#             f"deployed: {self.deployed})"
#         )

# def process_reports(report_list):
#     roster = {}
#     ranks = set()

#     for report in report_list:
#         parts = report.split("|")

#         name = parts[0].strip().title()
#         rank = parts[1].strip().upper()

#         fitness_part = parts[2].strip()
#         fitness = int(fitness_part.split(":")[1])

#         status_part = parts[3].strip()
#         status = status_part.split(":")[1].lower()

#         deployed = status == "deployed"

#         soldier = Soldier(name, rank, fitness, deployed)

#         roster[name] = soldier
#         ranks.add(rank)

#     return roster, ranks


# def show_available(roster):
#     available_names = []

#     for name, soldier in roster.items():
#         if soldier.deployed is False:
#             available_names.append(name)

#     available_names.sort()

#     print(f"Available soldiers: {available_names}")


# def dispatch(roster, name):
#     normalized_name = name.strip().title()

#     print(f"Dispatching {normalized_name}...", end=" ")

#     if normalized_name not in roster:
#         print(f"{normalized_name} was not found.")
#         return

#     soldier = roster[normalized_name]

#     if soldier.deployed:
#         print(f"{normalized_name} is already deployed.")
#     else:
#         soldier.dispatch()
#         print("Done. Status set to deployed.")

# roster, ranks = process_reports(reports)

# print("=== ROSTER LOADED ===")
# print(f"{len(roster)} soldiers on record.")
# print(f"Ranks on file: {ranks}")
# print()

# show_available(roster)
# print()

# dispatch(roster, "Santos")
# dispatch(roster, "Kowalski")
# dispatch(roster, "Miller")
# print()

# print("Updated status:")

# for name in ["Santos", "Kowalski"]:
#     soldier = roster[name]

#     if soldier.deployed:
#         status = "deployed"
#     else:
#         status = "available"

#     print(f"  {name:<9}: {status}")


###Problem 2###

# recipe_data = {
#     "omelette": ["eggs", "butter", "salt", "pepper", "cheese"],
#     "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "salt"],
#     "tomato pasta": ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
#     "grilled cheese": ["bread", "cheese", "butter"],
# }

# pantry_items = [
#     "eggs",
#     "butter",
#     "salt",
#     "pepper",
#     "cheese",
#     "milk",
#     "bread",
#     "garlic",
# ]

# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients

#     def can_make(self, pantry_set):
#         for ingredient in self.ingredients:
#             if ingredient not in pantry_set:
#                 return False

#         return True

#     def missing_ingredients(self, pantry_set):
#         missing = []

#         for ingredient in self.ingredients:
#             if ingredient not in pantry_set:
#                 missing.append(ingredient)

#         missing.sort()
#         return missing

# class Pantry:
#     def __init__(self, ingredients):
#         self.ingredients = set(ingredients)

#     def add_ingredients(self, extra_ingredients):
#         for ingredient in extra_ingredients:
#             self.ingredients.add(ingredient)

#     def has(self, ingredient):
#         return ingredient in self.ingredients

# def create_recipes(recipe_dictionary):
#     recipes = []

#     for name, ingredients in recipe_dictionary.items():
#         recipe = Recipe(name, ingredients)
#         recipes.append(recipe)

#     return recipes

# def check_recipes(recipes, pantry):
#     print("=== RECIPE CHECKER ===")

#     all_ingredients = set()

#     for recipe in recipes:
#         for ingredient in recipe.ingredients:
#             all_ingredients.add(ingredient)

#         if recipe.can_make(pantry.ingredients):
#             print(f"{recipe.name:<15}: CAN MAKE ✓")
#         else:
#             missing = recipe.missing_ingredients(pantry.ingredients)
#             print(f"{recipe.name:<15}: MISSING — {missing}")

#     sorted_ingredients = list(all_ingredients)
#     sorted_ingredients.sort()

#     print()
#     print(
#         f"All unique ingredients ({len(sorted_ingredients)}): "
#         f"{sorted_ingredients}"
#     )

# recipes = create_recipes(recipe_data)
# pantry = Pantry(pantry_items)

# check_recipes(recipes, pantry)

###Problem 3###

# class LyricAnalyzer:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#         cleaned_lyrics = lyrics.lower()

#         punctuation = [
#             ",",
#             ".",
#             "!",
#             "?",
#             "'",
#             '"',
#             ":",
#             ";",
#             "-",
#             "—",
#             "(",
#             ")",
#         ]

#         for mark in punctuation:
#             cleaned_lyrics = cleaned_lyrics.replace(mark, "")

#         self.words = cleaned_lyrics.split()

#     def count_words(self):
#         word_counts = {}

#         for word in self.words:
#             if word in word_counts:
#                 word_counts[word] += 1
#             else:
#                 word_counts[word] = 1

#         return word_counts

#     def unique_word_count(self):
#         unique_words = set(self.words)
#         return len(unique_words)

#     def most_common_word(self):
#         word_counts = self.count_words()

#         most_common = ""
#         highest_count = 0

#         for word, count in word_counts.items():
#             if count > highest_count:
#                 most_common = word
#                 highest_count = count

#         return most_common, highest_count

#     def print_report(self):
#         word_counts = self.count_words()

#         alphabetical_words = list(word_counts.keys())
#         alphabetical_words.sort()

#         print("=== WORD COUNT ===")

#         for word in alphabetical_words:
#             print(f"{word:<10}: {word_counts[word]}")

#         common_word, common_count = self.most_common_word()

#         print()
#         print(f"Unique words: {self.unique_word_count()}")
#         print(f"Most common word: '{common_word}' — {common_count} times")

# ## Don't sing the blues by Bohnes. Its a jam, 10/10 rating
# if __name__ == "__main__":
#     lyrics = """
# I was ridiculous
# Young Icarus
# I flew too close to the sun
# But we now reminisce
# That wickedness
# Was the ship that kept me on
# And every choice I made
# I wouldn't trade
# All that for anyone
# So don't you cry, cry, cry for me
# And don't sing the...
# Blues, blues, blues
# """

#     analyzer = LyricAnalyzer(lyrics)
#     analyzer.print_report()

###Problem 4###


# raw_data = [
#     "Simba, lion, 7, Africa",
#     "Pebbles, penguin, 3, Antarctica",
#     "Kovu, lion, 4, Africa",
#     "Bubbles, dolphin, 12, Ocean",
#     "Mango, parrot, 6, South America",
#     "Nala, lion, 5, Africa",
#     "Splash, dolphin, 8, Ocean",
#     "Crackers, parrot, 2, South America",
# ]


# class Animal:
#     def __init__(self, name, species, age, origin):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.origin = origin

#     def __str__(self):
#         return (
#             f"{self.name} "
#             f"({self.species}, {self.age} years, from {self.origin})"
#         )

#     def get_info(self):
#         print()
#         print(f"Name:    {self.name}")
#         print(f"Species: {self.species}")
#         print(f"Age:     {self.age}")
#         print(f"Origin:  {self.origin}")


# def build_registry(data):
#     registry = {}

#     for entry in data:
#         parts = entry.split(",")

#         name = parts[0].strip().title()
#         species = parts[1].strip().lower()
#         age = int(parts[2].strip())
#         origin = parts[3].strip().title()

#         animal = Animal(name, species, age, origin)

#         registry[name] = animal

#     return registry


# def analyze_registry(registry):
#     species_set = set()
#     origin_set = set()

#     for animal in registry.values():
#         species_set.add(animal.species)
#         origin_set.add(animal.origin)

#     print("=== ZOO REGISTRY BUILT ===")
#     print(f"{len(registry)} animals registered.")
#     print()
#     print(f"Unique species: {species_set}")
#     print(f"Animals come from {len(origin_set)} distinct regions.")


# if __name__ == "__main__":
#     registry = build_registry(raw_data)

#     analyze_registry(registry)

#     print()
#     search_name = input("Enter an animal name to look up: ")
#     search_name = search_name.strip().title()

#     if search_name in registry:
#         registry[search_name].get_info()
#     else:
#         print(f"{search_name} was not found.")