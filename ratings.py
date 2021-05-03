"""Restaurant rating lister."""


# Import the file into python code
restuarant_names_ratings = open("scores.txt")


# Declare our function to create a dictionary from the file data
def restuarant_ratings(restuarant_names_ratings):
    #split each line of document into restuarant and ratings

    names_and_ratings = {}
    for name in restuarant_names_ratings:
        key, value = name.split(":")
        value = value.rstrip()

        names_and_ratings[key] = value 

    # Iterate over the dictionary to create tuples
    for names, ratings in sorted(names_and_ratings.items()):
        print(f"{names} is rated at {ratings}")

    return names_and_ratings
    
names_and_ratings = restuarant_ratings(restuarant_names_ratings)
    # Sort ratings into alphabetical order
    # Print restuarant rating statement

#Allow users to add their own restuarants and ratings, add to the list. 

user_restuarant_names = input("Name of restuarant would you like to rate?")
user_restuarant_values = input("What is your rating of this restuarant?")

# Take in user values, add them to existing dictionary in the same fashion
def user_restuarant_ratings(user_names, user_values) :
   
    names_and_ratings[user_names] = user_values
    
    for names, ratings in sorted(names_and_ratings.items()):
        print(f"{names} is rated at {ratings}")

    return names_and_ratings

user_restuarant_ratings(user_restuarant_names, user_restuarant_values)
