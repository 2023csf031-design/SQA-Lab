"""Core logic for the Student Grade Manager sample project."""

PASS_MARK = 50.0


class GradeManager:
    """Stores student marks and calculates simple statistics."""

    def __init__(self):
        self._marks = {}

    def add_student(self, name, mark):
        """Add a student or update the mark of an existing student."""
        name = name.strip()
        if not name:
            raise ValueError("Student name cannot be empty.")
        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")
        self._marks[name] = float(mark)

    def remove_student(self, name):
        """Remove a student. Raises KeyError if the student does not exist."""
        del self._marks[name]

    def get_mark(self, name):
        """Return the mark of one student."""
        return self._marks[name]

    def average(self):
        """Return the class average, or 0.0 when there are no students."""
        if not self._marks:
            return 0.0
        return sum(self._marks.values()) / len(self._marks)

    def highest(self):
        """Return a (name, mark) tuple for the top student, or None."""
        if not self._marks:
            return None
        name = max(self._marks, key=self._marks.get)
        return name, self._marks[name]

    def lowest(self):
        """Return a (name, mark) tuple for the lowest student, or None."""
        if not self._marks:
            return None
        name = min(self._marks, key=self._marks.get)
        return name, self._marks[name]

    def grade_for(self, name):
        """Return the letter grade for a student."""
        return letter_grade(self.get_mark(name))

    def passed_students(self):
        """Return a sorted list of students who reached the pass mark."""
        return sorted(n for n, m in self._marks.items() if m >= PASS_MARK)

    def failed_students(self):
        """Return a sorted list of students below the pass mark."""
        return sorted(n for n, m in self._marks.items() if m < PASS_MARK)

    def report(self):
        """Return a list of report lines, one per student, sorted by name."""
        return [
            f"{name}: {mark:.1f} ({letter_grade(mark)})"
            for name, mark in sorted(self._marks.items())
        ]


def letter_grade(mark):
    """Convert a numeric mark into a letter grade."""
    if mark >= 85:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= PASS_MARK:
        return "D"
    return "F"
