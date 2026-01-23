#1495. Friendly Movies Streamed Last Month
#Easy (SQL)
#
#Table: TVProgram
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| program_date  | date    |
#| content_id    | int     |
#| channel       | varchar |
#+---------------+---------+
#(program_date, content_id) is the primary key for this table.
#This table contains information of the content broadcast in the TV.
#content_id is the id of the program in some channel on the TV.
#
#Table: Content
#+------------------+---------+
#| Column Name      | Type    |
#+------------------+---------+
#| content_id       | int     |
#| title            | varchar |
#| Kids_content     | enum    |
#| content_type     | varchar |
#+------------------+---------+
#content_id is the primary key for this table.
#Kids_content is an enum that takes one of the values ('Y', 'N') where:
#'Y' means is content for kids otherwise 'N' is not content for kids.
#content_type is the category of the content as movies, series, etc.
#
#Write an SQL query to report the distinct titles of the kid-friendly movies
#streamed in June 2020.
#
#Return the result table in any order.
#
#Example 1:
#Input:
#TVProgram table:
#+--------------------+--------------+-------------+
#| program_date       | content_id   | channel     |
#+--------------------+--------------+-------------+
#| 2020-06-10 08:00   | 1            | LC-Channel  |
#| 2020-05-11 12:00   | 2            | LC-Channel  |
#| 2020-05-12 12:00   | 3            | LC-Channel  |
#| 2020-05-13 14:00   | 4            | Disney Ch   |
#| 2020-06-18 14:00   | 4            | Disney Ch   |
#| 2020-07-15 16:00   | 5            | Disney Ch   |
#+--------------------+--------------+-------------+
#Content table:
#+------------+----------------+---------------+---------------+
#| content_id | title          | Kids_content  | content_type  |
#+------------+----------------+---------------+---------------+
#| 1          | Leetcode Movie | N             | Movies        |
#| 2          | Alg. for Kids  | Y             | Series        |
#| 3          | Database Coverage | N          | Movies        |
#| 4          | Aladdin        | Y             | Movies        |
#| 5          | Cinderella     | Y             | Movies        |
#+------------+----------------+---------------+---------------+
#Output:
#+--------------+
#| title        |
#+--------------+
#| Aladdin      |
#+--------------+

#SQL Solution:
#SELECT DISTINCT c.title
#FROM TVProgram t
#JOIN Content c ON t.content_id = c.content_id
#WHERE c.Kids_content = 'Y'
#  AND c.content_type = 'Movies'
#  AND t.program_date BETWEEN '2020-06-01' AND '2020-06-30';
#
#-- Alternative using YEAR and MONTH functions:
#-- SELECT DISTINCT c.title
#-- FROM TVProgram t
#-- JOIN Content c ON t.content_id = c.content_id
#-- WHERE c.Kids_content = 'Y'
#--   AND c.content_type = 'Movies'
#--   AND YEAR(t.program_date) = 2020
#--   AND MONTH(t.program_date) = 6;

from typing import List
from datetime import datetime

class Solution:
    def friendlyMoviesStreamedLastMonth(self, tv_program: List[dict], content: List[dict]) -> List[str]:
        """
        Python simulation of SQL query.
        """
        # Create content lookup
        content_info = {c['content_id']: c for c in content}

        # Find kid-friendly movies streamed in June 2020
        titles = set()

        for program in tv_program:
            date = program['program_date']
            if isinstance(date, str):
                date = datetime.strptime(date[:10], '%Y-%m-%d')

            # Check if June 2020
            if date.year == 2020 and date.month == 6:
                content_id = program['content_id']
                c = content_info.get(content_id)

                if c and c['Kids_content'] == 'Y' and c['content_type'] == 'Movies':
                    titles.add(c['title'])

        return list(titles)


class SolutionExplicit:
    def friendlyMoviesStreamedLastMonth(self, tv_program: List[dict], content: List[dict]) -> List[str]:
        """More explicit join simulation"""
        # Step 1: Filter content to kid-friendly movies
        kid_movies = {c['content_id']: c['title']
                      for c in content
                      if c['Kids_content'] == 'Y' and c['content_type'] == 'Movies'}

        # Step 2: Filter TV programs to June 2020
        june_2020_content_ids = set()
        for program in tv_program:
            date = program['program_date']
            if isinstance(date, str):
                date = datetime.strptime(date[:10], '%Y-%m-%d')

            if date.year == 2020 and date.month == 6:
                june_2020_content_ids.add(program['content_id'])

        # Step 3: Find intersection and get titles
        result = set()
        for content_id in june_2020_content_ids:
            if content_id in kid_movies:
                result.add(kid_movies[content_id])

        return list(result)
