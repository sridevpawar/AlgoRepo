
import heapq
def giveBooks(numStudents, numBooks, numPages):
  sorted(numPages)
  students = [(0, x) for x in range(numStudents)]
  books = [[] for x in range(numStudents)]
  pageIndex = 0
  heapq.heapify(students)
  while pageIndex < len(numPages):
    student = heapq.heappop(students)
    books[student[1]].append(numPages[pageIndex])
    heapq.heappush(students, (student[0] + numPages[pageIndex], student[1]))
    pageIndex += 1

  print(students)
  print(books)
    
    
giveBooks(2, 4, [12,90,67,34])