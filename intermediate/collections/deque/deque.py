"""The first data structure to be added to collections"""
# * enqueue - adding an item at the end of a queue
# * dequeue - removing an item at the end of a queue

from collections import deque

ticket_queue = deque()
print(ticket_queue)

ticket_queue.append("Sammy")
ticket_queue.append("Bob")
ticket_queue.append("Jeff")
ticket_queue.append("Jov")

print(ticket_queue)
print(ticket_queue.popleft())
print(ticket_queue.appendleft("Biko"))
print(ticket_queue)

# * maxlen argument
# once the maxlen has been reached adding a file at one end pops out
# a file on the opposite end
# when not provided, the deque can grow to an arbitrary number of length
recent_files = deque(["deque.py", "readme.md", "blogs.tsx"], maxlen=3)
recent_files.appendleft("pyproject.toml")
recent_files.appendleft("requirements.txt")
recent_files.appendleft("main.rs")
recent_files.append("main.py")
print(recent_files)

prime_numbers_less_than_ten = deque((2, 3, 5, 7))
print(prime_numbers_less_than_ten)
print(deque("pythagoras"))

# ! unlike lists, deque doesn't accept pop with arbitrary indices
# ! e.g deque("abcd").pop(2)

# extending an existing deque
numbers = deque([1, 2, 3])
numbers.extend([4, 5, 6])
print(numbers)
numbers.extendleft([0, -1, -2, -3, -4, -5, -6])
print(numbers)

# inserting at a given position
numbers.insert(len(numbers), 7)
numbers.insert(0, -7)
print(numbers)


ordinals = deque(["first", "second", "third"])
ordinals.rotate()
print(ordinals)
ordinals.rotate(2)
print(ordinals)
ordinals.rotate(-2)
print(ordinals)
ordinals.rotate(-1)
print(ordinals)
