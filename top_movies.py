movie_list = ['Die Hard', 'Forest Gump', 'Crash', 'Requiem for a Dream', 'Shrek']
count = 1

print("Here are my favorite movies:")
for movie in movie_list:
    print(str(count) + ".", movie)
    count += 1

movie_list.append(input("Please add one more movie: "))
print(movie_list)

count = 2
print("Here are the even movies: ")
for movie in [1, 3, 5]:
    print(str(count) + ".", movie_list[movie])
    count += 2
