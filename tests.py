from asyncio import constants
import unittest
import sys
import io
import program
import constants

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

class TestMultiValueDict(unittest.TestCase):
    def testAddSingle(self):
        program.initDict()
        out = handleInput("ADD foo bar")
        self.assertEqual(out.getvalue().strip(), constants.ADD_SUCCESS)

    def testAddCollision(self):
        program.initDict()
        program.processInput("ADD foo bar")
        out = handleInput("ADD foo bar")
        self.assertEqual(out.getvalue().strip(), constants.ERR_MEMBER_EXISTS)
    
    def testMembers(self):
        program.initDict()
        program.processInput("ADD foo bar")
        program.processInput("ADD foo baz")
        out = handleInput("MEMBERS foo")
        self.assertEqual(out.getvalue().strip(), "1) bar\n2) baz")

    




if __name__ == '__main__':
    unittest.main()