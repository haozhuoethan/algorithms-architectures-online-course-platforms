class LearningPathGenerator:
    def __init__(self, courses):
        self.courses = courses

    def recommend_courses(self, user):
        """Recommend courses based on user interests"""
        recommended_courses = []
        for course in self.courses:
            if any(tag in user.interests for tag in course.tags):
                recommended_courses.append(course)
        return recommended_courses