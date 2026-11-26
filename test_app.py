import unittest
import io
from contextlib import redirect_stdout
from app import main


class TestApp(unittest.TestCase):

    def test_greeting(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertIn("Hello, Jenkins!", output.getvalue())

    def test_ci_message(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertIn(
            "Continuous Integration is working!",
            output.getvalue()
        )


if __name__ == "__main__":
    unittest.main()
