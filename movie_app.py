# Create a variable called title_or_ratings, set to 1.
import string


title_or_ratings = 1
# You should be able to change this between 1, 2, and 3 to change what your program prints.


# Create a variable `movie_title` and set it to "Back to the Future".
movie_title = "Back to the Future"

# Create a variable `movie rating` to hold the rating and set it to `8`.
movie_rating = 8

# Create a function, print_movie_title, that prints the movie title.


def print_movie_title():
    print(movie_title)

# Create a function, print_movie_rating, that prints the movie rating.


def print_movie_rating():
    print(movie_rating)

# Create a function, print_single_movie_rating, that prints the string you had in lab 1.


def print_single_movie_rating(string: string):
    print("I had this " + string + " in lab 1")

# Create a function, print_all_ratings, that takes one argument movie_list.
# This prints "The movie <movie> has a great rating!"


def print_all_ratings(movie: string):
    print("The movie " + movie + " has a great rating!")


# Create one main function which will call everything else - subsituting function calls for the print statements.

def main():
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]
    if title_or_ratings == 1:
        print_movie_title()
    elif title_or_ratings == 2:
        print_movie_rating()
    elif title_or_ratings == 3:
        print_single_movie_rating()
    else:
        print("variable needs to be 1 or 2 or 3")
        # Inside the main function, create a default_movie_list with "Back to the Future", "Blade", and "Spirited Away"

        # Inside the main function, call the print_all_ratings function and pass it the default_movie_list as a parameter

        # Inside the main function, put your print statement from the previous lab but subsitute function calls.

        # If title_or_ratings is 1, call print_movie_title
        # If title_or_ratings is 2, call print_movie_rating().
        # If title_or_ratings is 3, call print_single_movie_rating()

        # Start with this prompt for your `main` function
        # It tells Python to go directly to the main function and run that
__name__ = "__main__"
if __name__ == "__main__":
    main()
