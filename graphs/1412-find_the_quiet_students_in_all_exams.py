#1412. Find the Quiet Students in All Exams
#Hard
#
#Table: Student
#+---------------------+---------+
#| Column Name         | Type    |
#+---------------------+---------+
#| student_id          | int     |
#| student_name        | varchar |
#+---------------------+---------+
#student_id is the primary key for this table.
#
#Table: Exam
#+---------------+---------+
#| Column Name   | Type    |
#+---------------+---------+
#| exam_id       | int     |
#| student_id    | int     |
#| score         | int     |
#+---------------+---------+
#(exam_id, student_id) is the primary key for this table.
#
#A quiet student is the one who took at least one exam and did not score the
#highest or the lowest score in any of the exams.
#
#Write an SQL query to report the students (student_id, student_name) being
#quiet in all exams. Do not return the student who has never taken any exam.
#
#Return the result table ordered by student_id.
#
#Example 1:
#Input:
#Student table:
#+-------------+---------------+
#| student_id  | student_name  |
#+-------------+---------------+
#| 1           | Daniel        |
#| 2           | Jade          |
#| 3           | Stella        |
#| 4           | Jonathan      |
#| 5           | Will          |
#+-------------+---------------+
#Exam table:
#+------------+--------------+-----------+
#| exam_id    | student_id   | score     |
#+------------+--------------+-----------+
#| 10         | 1            | 70        |
#| 10         | 2            | 80        |
#| 10         | 3            | 90        |
#| 20         | 1            | 80        |
#| 30         | 1            | 70        |
#| 30         | 3            | 80        |
#| 30         | 4            | 90        |
#| 40         | 1            | 60        |
#| 40         | 2            | 70        |
#| 40         | 4            | 80        |
#+------------+--------------+-----------+
#Output:
#+-------------+---------------+
#| student_id  | student_name  |
#+-------------+---------------+
#| 2           | Jade          |
#+-------------+---------------+
#Explanation:
#For exam 10: Student 1 and 3 hold the lowest and high scores respectively.
#For exam 20: Student 1 hold both highest and lowest score.
#For exam 30: Student 1 and 4 hold the lowest and high scores respectively.
#For exam 40: Student 1 and 4 hold the lowest and high scores respectively.
#Student 2 and 5 have never got the highest or lowest in any of the exams.
#Since student 5 has not taken any exam, the final output is only student 2.

#SQL Solution:
#WITH exam_stats AS (
#    SELECT exam_id, MIN(score) as min_score, MAX(score) as max_score
#    FROM Exam
#    GROUP BY exam_id
#),
#loud_students AS (
#    SELECT DISTINCT e.student_id
#    FROM Exam e
#    JOIN exam_stats es ON e.exam_id = es.exam_id
#    WHERE e.score = es.min_score OR e.score = es.max_score
#)
#SELECT s.student_id, s.student_name
#FROM Student s
#WHERE s.student_id IN (SELECT DISTINCT student_id FROM Exam)
#AND s.student_id NOT IN (SELECT student_id FROM loud_students)
#ORDER BY s.student_id;

from typing import List
from collections import defaultdict

class Solution:
    def findQuietStudents(self, students: List[dict], exams: List[dict]) -> List[dict]:
        """
        Python simulation of SQL query.
        Find students who took exams but never got highest or lowest score.
        """
        # Get students who took at least one exam
        students_with_exams = set(e['student_id'] for e in exams)

        # Get min/max score for each exam
        exam_scores = defaultdict(list)
        for e in exams:
            exam_scores[e['exam_id']].append((e['score'], e['student_id']))

        # Find "loud" students (got highest or lowest in any exam)
        loud_students = set()
        for exam_id, scores in exam_scores.items():
            if not scores:
                continue
            min_score = min(s[0] for s in scores)
            max_score = max(s[0] for s in scores)

            for score, student_id in scores:
                if score == min_score or score == max_score:
                    loud_students.add(student_id)

        # Quiet students = took exams AND never loud
        quiet_student_ids = students_with_exams - loud_students

        # Build result
        student_names = {s['student_id']: s['student_name'] for s in students}
        result = [
            {'student_id': sid, 'student_name': student_names[sid]}
            for sid in sorted(quiet_student_ids)
        ]

        return result


class SolutionExplicit:
    def findQuietStudents(self, students: List[dict], exams: List[dict]) -> List[dict]:
        """More explicit version"""
        # Group exams by exam_id
        exams_by_id = defaultdict(list)
        for e in exams:
            exams_by_id[e['exam_id']].append({
                'student_id': e['student_id'],
                'score': e['score']
            })

        # Track which students scored highest or lowest
        loud = set()
        all_exam_takers = set()

        for exam_id, exam_scores in exams_by_id.items():
            scores = [e['score'] for e in exam_scores]
            min_s, max_s = min(scores), max(scores)

            for e in exam_scores:
                all_exam_takers.add(e['student_id'])
                if e['score'] == min_s or e['score'] == max_s:
                    loud.add(e['student_id'])

        # Quiet = took exams but never loud
        quiet = all_exam_takers - loud

        # Map to names
        names = {s['student_id']: s['student_name'] for s in students}
        return [
            {'student_id': sid, 'student_name': names[sid]}
            for sid in sorted(quiet)
        ]
