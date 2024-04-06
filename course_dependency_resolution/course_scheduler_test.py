from course_scheduler import CourseScheduler

# Example Use Case
scheduler = CourseScheduler()
scheduler.add_course_dependency('Data Structures', 'Introduction to Programming')
scheduler.add_course_dependency('Algorithms', 'Data Structures')
scheduler.add_course_dependency('Advanced Algorithms', 'Algorithms')
scheduler.add_course_dependency('Machine Learning', 'Algorithms')
scheduler.add_course_dependency('Databases', 'Data Structures')
# scheduler.add_course_dependency('Introduction to Programming', 'Databases')  # Introduces a cycle

""""
if scheduler.find_all_cycles():
    print("Circular dependency detected!")
    suggestions = scheduler.find_resolution_suggestions()
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No circular dependencies detected.")
"""

# Assuming the user can handle 2 courses in parallel
optimized_schedule = scheduler.schedule_courses(parallel_capacity=2)
for term, courses in enumerate(optimized_schedule, start=1):
    print(f"Term {term}: {', '.join(courses)}")


# from course_scheduler import CourseScheduler

# Initialize the scheduler
scheduler = CourseScheduler()

# Add course dependencies
scheduler.add_course_dependency('Algorithms', 'Data Structures')

# Schedule courses
optimized_schedule = scheduler.schedule_courses(parallel_capacity=2)
print(optimized_schedule)

# Detect and resolve circular dependencies
if scheduler.find_all_cycles():
    print(scheduler.find_resolution_suggestions())