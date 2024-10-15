def display_course_details(course_dict, course_number):
    print(f"Course Number: {course_number}")
    print(f"Room Number: {course_dict['room_numbers'][course_number]}")
    print(f"Instructor: {course_dict['instructors'][course_number]}")
    print(f"Meeting Time: {course_dict['meeting_times'][course_number]}")

course_data = {
    'room_numbers': {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'NT110': '1244',
        'CM241': '1411'
    },
    'instructors': {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    },
    'meeting_times': {
        'CS101': '8:00 a.m.',
        'CS102': '9:00 a.m.',
        'CS103': '10:00 a.m.',
        'NT110': '11:00 a.m.',
        'CM241': '1:00 p.m.'
    }
}

course_num = input("Enter a course number: ")

# Display details for the entered course number
if course_num in course_data['room_numbers']:
    display_course_details(course_data, course_num)
else:
    print("Course number not found.")
