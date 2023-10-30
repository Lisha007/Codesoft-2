def get_greeting(name):
    return f"{name}, welcome to moviechat! May I suggest you a movie according to your mood?"

def determine_mood():
    print("Please enter your mood from the following options: action, comedy, drama, sci-fi, horror, animated, romantic")

def suggest_movie(user_input):
    user_input = user_input.lower()
    suggested_movies = []

    for category in movie_rules:
        if category in user_input:
            suggested_movies.extend(movie_rules[category])

    if suggested_movies:
        return suggested_movies
    else:
        return ["Sorry, I couldn't find any movies in that category."]

def main_chat_loop():
    print("Hello! Type 'goodbye' to exit.")
    user_name = input("moviechat: May I know your name? ")
    print("moviechat:", get_greeting(user_name))

    while True:
        user_input = input(f"{user_name}: ").lower()
        if user_input == 'goodbye':
            print("moviechat: Goodbye!")
            break
        elif user_input == 'yes':
            determine_mood()
        elif user_input == 'no':
            print("moviechat: Alright, if you ever change your mind, feel free to ask. Goodbye!")
            break
        else:
            suggestions = suggest_movie(user_input)
            print("moviechat:", suggestions)

movie_rules = {
    "hi": ['Hello!', 'Hi there!', 'Hey!'],
    "how are you?": ['I am good, thank you!', 'Feeling great, thanks for asking.'],
    "what is your name?": ['I am a chatbot.'],
    "your name?": ['I am just a bot.', 'My name is ChatBot.'],
    "exit": ['Goodbye!', 'See you later!'],
    "action": ["Pathaan", "Jawaan", "URI-The Surgical Strike", "Master"],
    "comedy": ["Pagalpanti", "Ludo", "Ludo", "Newton"],
    "drama": ["All the Best", "Forrest Gump", "The Godfather", "Golmaal"],
    "sci-fi": ["Blade Runner 2049", "Interstellar", "The Matrix", "Arrival"],
    "horror": ["The Conjuring", "1920 Evil Returns", "A Quiet Place", "Hereditary"],
    "animated": ["Mahabharat", "Bal Ganesh", "Kochadaiiyaan", "Finding Nemo"],
    "romantic": ["Gehraiyaan", "La La Land", "October", "Shiddat"]
}

main_chat_loop()
