
print("Part 1. Make a list of movies and print the list.")
print("   ")
movie_list = ['Die Hard', 'Forest Gump', 'Crash', 'Requiem for a Dream', 'Shrek']
count = 1

print("Here are my favorite movies:")
for movie in movie_list:
    print(str(count) + ".", movie)
    count += 1
print("   ")
print("Part 2. Add a movie to the list based on user input.")
print("   ")
movie_list = ['Die Hard', 'Forest Gump', 'Crash', 'Requiem for a Dream', 'Shrek']
user_movie = [input("Please add one more movie: ")]
movie_list = movie_list + user_movie

print(movie_list)

print("   ")
print("Part 3. Print ONLY the even INDEXED movies.")
print("   ")

even_movies = []
odd_movies = []
count = 2


print("Here are the even movies: ")
for movie in range(0, len(movie_list)):
    if movie % 2:
        even_movies.append(movie_list[movie])
    else:
        odd_movies.append(movie_list[movie])

for movie in even_movies:
    print(str(count) + ".", movie)
    count +=2