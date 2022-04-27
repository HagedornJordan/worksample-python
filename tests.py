import unittest
import sys
import io
import program

def handleInput(input):
    ogErr = sys.stderr
    ogOut = sys.stdout
    out = io.StringIO()
    sys.stderr = out
    sys.stdout = out
    program.processInput(input)
    sys.stdout = ogOut
    sys.stderr = ogErr
    return out

class TestInputValidation(unittest.TestCase):
    def testAdd(self):
        out = handleInput("ADD a")
        self.assertEqual(out.getvalue().strip(), "Invalid number of args for command ADD. Expected (2), got (1).")


if __name__ == '__main__':
    unittest.main()