from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_q = deque(students)
        sandwich_stack = deque(sandwiches)

        unable_to_eat = 0

        while student_q and unable_to_eat < len(student_q):
            if (student_q[0] == sandwich_stack[0]):
                student_q.popleft()
                sandwich_stack.popleft()
                unable_to_eat = 0
            else:
                student_q.append(student_q.popleft())
                unable_to_eat += 1
        return len(student_q)
        