# Movie class
class Movie:
    def __init__(self, name, rating, ticket_price):
        self.name = name
        self.rating = rating
        self.ticket_price = ticket_price
        self.category = self.categorize_movie()

    def categorize_movie(self):
        # Categorization based on rating
        if self.rating >= 8:
            return "Hit"
        elif 5 <= self.rating < 8:
            return "Average"
        else:
            return "Flop"

    def display_info(self):
        print(f"Movie: {self.name}, Rating: {self.rating}, "
              f"Ticket Price: {self.ticket_price}, Category: {self.category}")


# Cinema class
class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Movie '{movie.name}' added successfully!")

    def display_movies(self):
        if not self.movies:
            print("No movies in the collection.")
        else:
            print("\n--- Cinema Movie Collection ---")
            for movie in self.movies:
                movie.display_info()


# Example usage
if __name__ == "__main__":
    cinema = Cinema()

    # Adding movies
    movie1 = Movie("Inception", 9, 300)
    movie2 = Movie("Random Comedy", 6, 200)
    movie3 = Movie("Unknown Horror", 4, 150)

    cinema.add_movie(movie1)
    cinema.add_movie(movie2)
    cinema.add_movie(movie3)

    # Display all movies
    cinema.display_movies()
