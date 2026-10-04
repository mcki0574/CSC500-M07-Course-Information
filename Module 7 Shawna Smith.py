# Course Information System
# CSC500 Module 7

# Dictionary containing course room numbers
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Dictionary containing course instructors
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Dictionary containing course meeting times
# Replace these values with the actual meeting times provided by your instructor.
course_times = {
    "CSC101": "TBD",
    "CSC102": "TBD",
    "CSC103": "TBD",
    "NET110": "TBD",
    "COM241": "TBD"
}

# Prompt the user for a course number
course_number = input("Enter a course number (example: CSC101): ").strip().upper()

# Check whether the course exists
if course_number in course_rooms:
    print("\nCourse Information")
    print("----------------------------")
    print(f"Course Number: {course_number}")
    print(f"Room Number:   {course_rooms[course_number]}")
    print(f"Instructor:    {course_instructors[course_number]}")
    print(f"Meeting Time:  {course_times[course_number]}")
else:
    print(f"\nSorry, {course_number} was not found.")
    print("Please enter a valid course number.")