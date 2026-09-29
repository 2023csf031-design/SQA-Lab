"""Command line demo for the Student Grade Manager."""

from grade_manager import GradeManager


def main():
    manager = GradeManager()
    manager.add_student("Ayesha", 91)
    manager.add_student("Bilal", 67.5)
    manager.add_student("Hina", 48)
    manager.add_student("Usman", 76)

    print("Student Report")
    for line in manager.report():
        print(line)

    print(f"Class average: {manager.average():.2f}")
    print(f"Top student: {manager.highest()[0]}")
    print(f"Passed: {', '.join(manager.passed_students())}")
    print(f"Failed: {', '.join(manager.failed_students())}")


if __name__ == "__main__":
    main()
