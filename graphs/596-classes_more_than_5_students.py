#596. Classes More Than 5 Students
#Easy
#
#Table: Courses
#+-------------+---------+
#| Column Name | Type    |
#+-------------+---------+
#| student     | varchar |
#| class       | varchar |
#+-------------+---------+
#(student, class) is the primary key.
#
#Write a solution to find all the classes that have at least five students.
#Return the result table in any order.

# SQL Solution:
# SELECT class
# FROM Courses
# GROUP BY class
# HAVING COUNT(student) >= 5;

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """Pandas solution"""
    # Count students per class
    class_counts = courses.groupby('class').size().reset_index(name='count')

    # Filter classes with 5+ students
    result = class_counts[class_counts['count'] >= 5]

    return result[['class']]


def find_classes_alt(courses: pd.DataFrame) -> pd.DataFrame:
    """Alternative using value_counts"""
    counts = courses['class'].value_counts()
    classes = counts[counts >= 5].index.tolist()
    return pd.DataFrame({'class': classes})
