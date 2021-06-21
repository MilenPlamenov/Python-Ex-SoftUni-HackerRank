import sys
seen_movies = int(input())
worst_movie_rate = sys.maxsize
worst_name = ""
best_movie_rate = - sys.maxsize
best_name = ""
average_rating = 0
for all_seen_movies in range(seen_movies):
    movie_name = input()
    movie_rate = float(input())
    if movie_rate > best_movie_rate:
        best_name = movie_name
        best_movie_rate = movie_rate
    elif movie_rate < worst_movie_rate:
        worst_name = movie_name
        worst_movie_rate = movie_rate

    average_rating += movie_rate


print(f"{best_name} is with highest rating: {best_movie_rate:.1f}")
print(f"{worst_name} is with lowest rating: {worst_movie_rate:.1f}")
print(f"Average rating: {(average_rating / seen_movies):.1f}")