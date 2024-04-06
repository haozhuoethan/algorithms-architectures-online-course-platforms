# algorithms-architectures-online-course-platforms

## Installation

- Clone the repository to your local machine:

```
git clone git@github.com:haozhuoethan/algorithms-architectures-online-course-platforms.git
```

## Algorithms and Architectures List

### Course Dependency Resolution

#### Description

The Course Dependency Resolution is designed to optimize educational course planning and scheduling. It offers an automated solution to manage course prerequisites, schedule courses considering parallel enrollment capacities, and intelligently detect and suggest resolutions for circular dependencies within course structures. This project aims to assist academic institutions in creating efficient, logical, and flexible course schedules that enhance the learning experience.

#### Features

- **Course Dependency Management**: Add and manage course prerequisites in a directed graph structure to easily visualize and manipulate course dependencies.
- **Parallel Course Enrollment Scheduling**: Automatically schedule courses within terms, taking into account students' capacity for parallel enrollment, to minimize overall completion time.
- **Circular Dependency Detection**: Detect circular dependencies in course prerequisites, ensuring the curriculum structure is feasible for students to complete.
- **Dynamic Resolution Suggestions**: Analyze detected circular dependencies and suggest specific courses or dependencies for modification or removal to resolve cycles with minimal curriculum impact.

#### Prerequisites

- Python 3.6 or later

#### Usage

To use the Course Dependency Resolution, import and instantiate the `CourseScheduler` class from your Python script or interactive environment:

```python
from course_scheduler import CourseScheduler

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
```

#### Test

1. Navigate to the `course_dependency_resolution` directory:
   ```
   cd course_dependency_resolution
   ```
1. Run the `course_scheduler_test.py` script:
   ```
   python course_scheduler_test.py
   ```

### Scalable Video Streaming Architecture for Educational Content

[Scalable Video Streaming Architecture](scalable_video_streaming_architecture.md) - see the Scalable Video Streaming Architecture file for details.

### Personalized Learning Path Generation Algorithm

#### Overview

This project provides a basic implementation of a personalized learning path generation algorithm. It aims to recommend educational courses to users based on their individual interests. The algorithm matches user interests with course tags to generate a set of personalized course recommendations.

#### Features

- **User Interest-Based Recommendations**: Generates course recommendations based on the intersection of user interests and course tags.
- **Simple Data Model**: Utilizes straightforward `User` and `Course` classes for easy understanding and extensibility.

#### Prerequisites

- Python 3.x

#### Usage

1. Define courses with relevant tags and users with their interests.
2. Instantiate the `LearningPathGenerator` with the list of courses.
3. Use the `recommend_courses` method to generate personalized course recommendations for each user.

```python
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
```

#### Test

1. Navigate to the `personalized_learning_path_generation` directory:
   ```
   cd personalized_learning_path_generation
   ```
1. Run the `personalized_learning_path_test.py` script:
   ```
   python personalized_learning_path_test.py
   ```

#### Extending the Project

To make the algorithm more robust, consider implementing the following enhancements:

- **Dynamic User Profiling**: Incorporate machine learning to dynamically update user profiles based on their interactions and feedback.
- **Complex Matching Logic**: Improve the course recommendation logic by considering factors like course difficulty, user skill level, and learning goals.
- **Data Persistence**: Integrate a database to store user profiles, course catalogs, and interaction logs for long-term analysis.

## Contributing

Contributions to this project are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped to improve this project.
- Special thanks to academic advisors and curriculum planners for their insights and feedback.
