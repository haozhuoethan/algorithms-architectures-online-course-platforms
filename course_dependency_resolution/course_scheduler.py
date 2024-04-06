from collections import defaultdict, deque

class CourseScheduler:
    def __init__(self):
        # Course -> List of courses that depend on it
        self.graph = defaultdict(list)
        # Course -> Number of prerequisites
        self.in_degrees = defaultdict(int)

    def add_course_dependency(self, course, prerequisite):
        """Add a prerequisite relationship between two courses."""
        self.graph[prerequisite].append(course)
        self.in_degrees[course] += 1
        if course not in self.graph:
            self.graph[course] = []

    def schedule_courses(self, parallel_capacity):
        """Schedule courses given the parallel enrollment capacity."""
        # Initialize a queue with courses having no prerequisites
        queue = deque([course for course in self.graph if self.in_degrees[course] == 0])
        schedule = []  # List to store the scheduled courses in order

        while queue:
            # Current batch of courses to take in parallel, limited by parallel_capacity
            current_batch = []
            for _ in range(min(len(queue), parallel_capacity)):
                course = queue.popleft()
                current_batch.append(course)
                # Decrease in-degree for dependent courses
                for dependent in self.graph[course]:
                    self.in_degrees[dependent] -= 1
                    # If in-degree becomes 0, add it to the queue
                    if self.in_degrees[dependent] == 0:
                        queue.append(dependent)
            schedule.append(current_batch)

        return schedule
    
    def find_all_cycles(self):
        def dfs(course, visited, stack, path, cycles):
            if course in stack:
                cycle_index = stack.index(course)
                cycles.append(path[cycle_index:])
                return
            if course in visited:
                return

            visited.add(course)
            stack.append(course)

            for next_course in self.graph[course]:
                dfs(next_course, visited, stack, path + [next_course], cycles)

            stack.pop()

        visited = set()
        cycles = []
        for course in self.graph:
            dfs(course, visited, [course], [course], cycles)

        return cycles

    def evaluate_cycle_impact(self, cycle):
        # Placeholder for a more sophisticated impact evaluation
        # For simplicity, suggesting removing the course with the highest number of dependencies
        most_dependent_course = max(cycle, key=lambda x: len(self.graph[x]))
        return most_dependent_course

    def find_resolution_suggestions(self):
        cycles = self.find_all_cycles()
        if not cycles:
            return "No circular dependencies detected."

        suggestions = []
        for cycle in cycles:
            course_to_adjust = self.evaluate_cycle_impact(cycle)
            suggestions.append(f"Consider removing or adjusting the course '{course_to_adjust}' to resolve the cycle: {' -> '.join(cycle)}.")

        return suggestions
