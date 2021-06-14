
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
#movie_list = ['Die Hard', 'Forest Gump', 'Crash', 'Requiem for a Dream', 'Shrek']
user_movie = input("Please add one more movie: ")
#avoid list concat
movie_list.append(user_movie)

print(movie_list)

print("   ")
print("Part 3. Print ONLY the even INDEXED movies.")
#Use the range() to iterate through even indexed movies instead of creating new lists
print("   ")

print("Here are the even movies: ")
for movie in range(0, len(movie_list), 2):
    print((str(movie)) + ".", movie_list[movie])