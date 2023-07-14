from unittest import TestCase
from Exercise7Task4 import evolve


class EvolveTestSuite(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
                        "--------------",
                        "| ###        |",
                        "| #          |",
                        "|  #         |",
                        "|            |",
                        "|            |",
                        "--------------"
                    ), 5)
        actual = evolve(field, 4)

    def test_tuple(self):
        with self.assertRaises(Warning):
            evolve((5, 5, 3), 5)

    def test_wrong_char1(self):
        with self.assertRaises(Warning):
            field = (
                "--------------",
                "| ###        -",
                "| #          |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)

    def test_wrong_char2(self):
        with self.assertRaises(Warning):
            field = (
                "-------------",
                "|        f    |",
                "|  ###       |",
                "|  #         |",
                "|   #        |",
                "|            |",
                "--------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)

    def test_wrong_char3(self):
        with self.assertRaises(Warning):
            field = (
                "------------|-",
                "| ###        |",
                "| #          |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)

    def test_wrong_char4(self):
        with self.assertRaises(Warning):
            field = (
                "--------------",
                "| ###        |",
                "| #         - |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)

    def test_wrong_char5(self):
        with self.assertRaises(Warning):
            field = (
                "--------------",
                "| ###       -|",
                "| #          |",
                "|  #         |",
                "|            |",
                "|            |",
                "--------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)

    def test_incorrect_num(self):
        with self.assertRaises(Warning):
            field = (
                "--------------",
                "|            |",
                "|  ###       |",
                "|  #         |",
                "|   #        |",
                "|            |",
                "--------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, -4)

    def test_wrong_size(self):
        with self.assertRaises(Warning):
            field = (
                "--------------",
                "|            |",

            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)

    def test_incorrect_line_length(self):
        with self.assertRaises(Warning):
            field = (
                "--------------",
                "|            |",
                "|  ###       |",
                "|  #         |",
                "|   #        |",
                "|            |",
                "------------"
            )
            expected = ((
                            "--------------",
                            "| ###        |",
                            "| #          |",
                            "|  #         |",
                            "|            |",
                            "|            |",
                            "--------------"
                        ), 5)
            actual = evolve(field, 4)
