#1341. Movie Rating
#Medium
#
#Table: Movies
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| movie_id      | int     |
#| title         | varchar |
#+---------------+---------+
#movie_id is the primary key for this table.
#
#Table: Users
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| user_id       | int     |
#| name          | varchar |
#+---------------+---------+
#user_id is the primary key for this table.
#
#Table: MovieRating
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| movie_id      | int     |
#| user_id       | int     |
#| rating        | int     |
#| created_at    | date    |
#+---------------+---------+
#(movie_id, user_id) is the primary key for this table.
#
#Write an SQL query to:
#1. Find the name of the user who has rated the greatest number of movies.
#   In case of a tie, return the lexicographically smaller user name.
#2. Find the movie name with the highest average rating in February 2020.
#   In case of a tie, return the lexicographically smaller movie name.

# SQL Solution:
# (
#     SELECT u.name AS results
#     FROM Users u
#     JOIN MovieRating mr ON u.user_id = mr.user_id
#     GROUP BY u.user_id, u.name
#     ORDER BY COUNT(*) DESC, u.name ASC
#     LIMIT 1
# )
# UNION ALL
# (
#     SELECT m.title AS results
#     FROM Movies m
#     JOIN MovieRating mr ON m.movie_id = mr.movie_id
#     WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
#     GROUP BY m.movie_id, m.title
#     ORDER BY AVG(mr.rating) DESC, m.title ASC
#     LIMIT 1
# );

# Python simulation
from typing import List, Tuple
from datetime import date
from collections import defaultdict

class Solution:
    def movieRating(
        self,
        movies: List[Tuple[int, str]],
        users: List[Tuple[int, str]],
        ratings: List[Tuple[int, int, int, date]]
    ) -> List[str]:
        """
        1. User with most ratings (tie: lexicographically smaller)
        2. Movie with highest avg rating in Feb 2020 (tie: lexicographically smaller)
        """
        # Create mappings
        movie_titles = {mid: title for mid, title in movies}
        user_names = {uid: name for uid, name in users}

        # Count ratings per user
        user_rating_count = defaultdict(int)
        for movie_id, user_id, rating, created in ratings:
            user_rating_count[user_id] += 1

        # Find user with most ratings
        max_count = max(user_rating_count.values())
        top_users = [uid for uid, count in user_rating_count.items() if count == max_count]
        top_user = min(top_users, key=lambda uid: user_names[uid])

        # Calculate average rating per movie in Feb 2020
        feb_ratings = defaultdict(list)
        for movie_id, user_id, rating, created in ratings:
            if created.year == 2020 and created.month == 2:
                feb_ratings[movie_id].append(rating)

        # Find movie with highest average
        movie_avgs = {mid: sum(r)/len(r) for mid, r in feb_ratings.items()}
        max_avg = max(movie_avgs.values())
        top_movies = [mid for mid, avg in movie_avgs.items() if avg == max_avg]
        top_movie = min(top_movies, key=lambda mid: movie_titles[mid])

        return [user_names[top_user], movie_titles[top_movie]]
