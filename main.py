# Define the characteristics and facts
characteristics = [
    "is alive",
    "eats meat",
    "eats plants",
    "has wings",
    "has fur",
    "has scales",
    "swims",
    "flies",
    "hunts at night",
    "nocturnal",
    "diurnal",
    "omnivorous",
    "has long neck",
    "lives in water",
    "lives in trees",
    "lives in burrows",
    "jumps",
    "camouflaged",
    "hunts in packs",
]

facts = {
    "carnivorous": ["eats meat"],
    "herbivorous": ["eats plants"],
    "animal": ["is alive"],
    "bird": ["has wings", "flies"],
    "mammal": ["has fur"],
    "reptile": ["has scales"],
    "fish": ["swims"],
    "lion": ["carnivorous", "animal"],
    "giraffe": ["herbivorous", "animal"],
    "eagle": ["diurnal", "bird"],
    "snake": ["carnivorous", "reptile"],
    "dolphin": ["swims", "animal"],
    "bat": ["flies", "hunts at night", "mammal"],
    "kangaroo": ["herbivorous", "jumps", "mammal"],
    "chameleon": ["camouflaged", "diurnal", "reptile"],
    "wolf": ["carnivorous", "hunts in packs", "mammal"],
    "elephant": ["herbivorous", "mammal"],
}
def ask_yes_or_no_question(characteristic):
    while True:
        answer = input(f"Does it {characteristic}? (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer

def match_facts(user_answers, facts):
    user_characteristics = []
    for i in range(len(characteristics)):
        if user_answers[i] == "yes":
            user_characteristics.append(characteristics[i])

    matching_objects = []
    max_guesses = 0
    for object_name, object_characteristics in facts.items():
        if all(characteristic in user_characteristics for characteristic in object_characteristics):
            user_characteristics.append(object_name)

            if len(object_characteristics) < max_guesses:
                continue

            if len(object_characteristics) == max_guesses:
                matching_objects.append(object_name)
                continue

            matching_objects = [object_name]
            max_guesses = len(object_characteristics)
    return matching_objects

def run(characteristics, facts):
    print("Welcome to the Guess My Object game!")
    print("I will ask you questions about some characteristics, and I will try to guess the object based on your answers.")

    user_answers = []

    # Ask user for yes/no answers and add "mammals" if they answer "yes" to "eats milk"
    for characteristic in characteristics:
        answer = ask_yes_or_no_question(characteristic)
        user_answers.append(answer)

    matching_objects = match_facts(user_answers, facts)

    if matching_objects:
        if len(matching_objects) == 1:
            print(f"My guess is that you're thinking of a {matching_objects[0]}.")
        else:
            print("I have a few guesses based on your answers:")
            for obj in matching_objects:
                print(obj)
    else:
        print("I couldn't guess the object based on your answers. It might not be in my knowledge base.")

if __name__ == "__main__":
    run(characteristics, facts)
