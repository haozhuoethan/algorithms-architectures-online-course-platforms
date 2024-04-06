from user import User
from course import Course
from learning_path_generator import LearningPathGenerator

# Sample Data
courses = [
    Course(1, "Introduction to Python", ["programming", "python"]),
    Course(2, "Advanced Python", ["programming", "python", "advanced"]),
    Course(3, "Data Science Basics", ["data science", "statistics"]),
    Course(4, "Machine Learning", ["data science", "machine learning"])
]

users = [
    User(1, ["python"]),
    User(2, ["data science", "machine learning"])
]

# Generate Learning Paths
generator = LearningPathGenerator(courses)

for user in users:
    print(f"Recommendations for User {user.id}:")
    recommendations = generator.recommend_courses(user)
    for course in recommendations:
        print(f"- {course.title}")
    print("")
