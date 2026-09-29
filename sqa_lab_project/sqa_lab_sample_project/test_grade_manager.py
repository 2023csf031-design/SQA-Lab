"""Unit tests for the Student Grade Manager."""

import unittest

from grade_manager import GradeManager, letter_grade


class TestLetterGrade(unittest.TestCase):
    def test_boundaries(self):
        self.assertEqual(letter_grade(100), "A")
        self.assertEqual(letter_grade(85), "A")
        self.assertEqual(letter_grade(84.9), "B")
        self.assertEqual(letter_grade(70), "B")
        self.assertEqual(letter_grade(60), "C")
        self.assertEqual(letter_grade(50), "D")
        self.assertEqual(letter_grade(49.9), "F")
        self.assertEqual(letter_grade(0), "F")


class TestGradeManager(unittest.TestCase):
    def setUp(self):
        self.manager = GradeManager()
        self.manager.add_student("Ayesha", 90)
        self.manager.add_student("Bilal", 60)
        self.manager.add_student("Hina", 40)

    def test_add_and_get_mark(self):
        self.assertEqual(self.manager.get_mark("Ayesha"), 90.0)

    def test_update_existing_student(self):
        self.manager.add_student("Ayesha", 95)
        self.assertEqual(self.manager.get_mark("Ayesha"), 95.0)

    def test_name_is_trimmed(self):
        self.manager.add_student("  Usman  ", 70)
        self.assertEqual(self.manager.get_mark("Usman"), 70.0)

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("   ", 50)

    def test_invalid_marks_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("Zara", 101)
        with self.assertRaises(ValueError):
            self.manager.add_student("Zara", -1)

    def test_remove_student(self):
        self.manager.remove_student("Hina")
        with self.assertRaises(KeyError):
            self.manager.get_mark("Hina")

    def test_remove_missing_student(self):
        with self.assertRaises(KeyError):
            self.manager.remove_student("Nobody")

    def test_average(self):
        self.assertAlmostEqual(self.manager.average(), 63.3333, places=3)

    def test_highest_and_lowest(self):
        self.assertEqual(self.manager.highest(), ("Ayesha", 90.0))
        self.assertEqual(self.manager.lowest(), ("Hina", 40.0))

    def test_empty_manager(self):
        empty = GradeManager()
        self.assertEqual(empty.average(), 0.0)
        self.assertIsNone(empty.highest())
        self.assertIsNone(empty.lowest())

    def test_grade_for(self):
        self.assertEqual(self.manager.grade_for("Ayesha"), "A")
        self.assertEqual(self.manager.grade_for("Hina"), "F")

    def test_passed_and_failed(self):
        self.assertEqual(self.manager.passed_students(), ["Ayesha", "Bilal"])
        self.assertEqual(self.manager.failed_students(), ["Hina"])

    def test_report(self):
        self.assertEqual(
            self.manager.report(),
            ["Ayesha: 90.0 (A)", "Bilal: 60.0 (C)", "Hina: 40.0 (F)"],
        )


if __name__ == "__main__":
    unittest.main()
