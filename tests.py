import unittest
import sys
import io
import program
import constants
import random

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

def randAscii():
    return random.randint(constants.MIN_ASCII, constants.MAX_ASCII)

class TestInputValidation(unittest.TestCase):
    def testAdd(self):
        out = handleInput("ADD a")
        self.assertEqual(out.getvalue().strip(), "Invalid number of args for command ADD. Expected (2), got (1).")

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

class TestMultiValueDict(unittest.TestCase):
    def testKeys(self):
        program.initDict()
        self.assertTrue(len(program.keys()) == 0)
        program.add("foo", "bar")
        keyInKeys = "foo" in program.keys()
        valInKeys = "bar" in program.keys()
        self.assertTrue(keyInKeys)
        self.assertFalse(valInKeys)

    def testMembers(self):
        program.initDict()
        program.add("foo", "bar")
        program.add("foo", "baz")
        allMembers = program.members("foo")
        self.assertTrue("bar" in allMembers)
        self.assertTrue("baz" in allMembers)
        self.assertFalse("biz" in allMembers)
        self.assertTrue(len(allMembers) == 2)
        self.assertTrue(not program.members("fii"))

    def testAdd(self):
        program.initDict()
        self.assertTrue(program.add("foo", "bar"))
        self.assertTrue(program.add("foo", "baz"))
        self.assertFalse(program.add("foo", "bar"))

    def testRemove(self):
        program.initDict()
        program.add("foo", "bar")
        program.add("foo", "baz")
        self.assertTrue(program.remove("foo", "bar") == 0)
        self.assertTrue(program.remove("foo", "bar") == 1)
        self.assertTrue("foo" in program.keys())
        self.assertTrue("bar" not in program.members("foo"))
        self.assertFalse(program.remove("foo", "bar") == 0)
        self.assertTrue(program.remove("foo", "baz") == 0)
        self.assertTrue(len(program.keys()) == 0)
        self.assertTrue(program.remove("boom", "pow") == 2)
    
    def testRemoveAll(self):
        program.initDict()
        program.add("foo", "bar")
        program.add("foo", "baz")
        program.add("fizz", "buzz")
        self.assertTrue(program.removeAll("foo"))
        self.assertTrue(len(program.keys()) == 1)
        self.assertFalse(program.removeAll("foo"))
        self.assertTrue("fizz" in program.keys())
        self.assertTrue("buzz" in program.members("fizz"))

    def testClear(self):
        program.initDict()
        program.add("foo", "bar")
        program.add("foo", "baz")
        program.add("fizz", "buzz")
        program.add("fii", "bar")
        program.add("fii", "baz")
        self.assertTrue(len(program.keys()) == 3)
        program.clear()
        self.assertTrue(len(program.keys()) == 0)
        self.assertTrue(len(program.members("foo")) == 0)

    def testKeyExists(self):
        program.initDict()
        self.assertFalse(program.keyExists("foo"))
        program.add("foo", "bar")
        self.assertTrue(program.keyExists("foo"))

    def testMemberExists(self):
        program.initDict()
        self.assertFalse(program.memberExists("foo", "bar"))
        program.add("foo", "bar")
        self.assertTrue(program.memberExists("foo", "bar"))
        self.assertFalse(program.memberExists("foo", "baz"))
        program.remove("foo", "bar")
        self.assertFalse(program.memberExists("foo", "bar"))

    def testAllMembers(self):
        program.initDict()
        allMembers = program.allMembers()
        self.assertTrue(len(allMembers) == 0)
        program.add("foo", "bar")
        program.add("foo", "baz")

        allMembers = program.allMembers()
        self.assertTrue(len(allMembers) == 2)
        program.add("bang", "bar")
        program.add("bang", "baz")

        allMembers = program.allMembers()
        self.assertTrue(len(allMembers) == 4)
        self.assertTrue("baz" in allMembers)
        self.assertTrue("bar" in allMembers)
        self.assertFalse("foo" in allMembers)
        self.assertFalse("bang" in allMembers)

    def testItems(self):
        program.initDict()
        allItems = program.items()
        self.assertTrue(len(allItems) == 0)
        program.add("foo", "bar")
        program.add("foo", "baz")

        allItems = program.items()
        self.assertTrue("foo: bar" in allItems)
        self.assertTrue("foo: baz" in allItems)
        self.assertFalse("fizz: baz" in allItems)

        program.add("bang", "bar")
        program.add("bang", "baz")

        allItems = program.items()
        self.assertTrue(len(allItems) == 4)
        self.assertTrue("foo: bar" in allItems)
        self.assertTrue("foo: baz" in allItems)
        self.assertTrue("bang: bar" in allItems)
        self.assertTrue("bang: baz" in allItems)
        self.assertFalse("fizz: baz" in allItems)

class StressTest(unittest.TestCase):
    def testMultiAdd(self):
        program.initDict()
        successes = 0
        for i in range(constants.PAIRS_TO_GENERATE):
            keyLen = random.randint(1, constants.MAX_KEY_LEN)
            valLen = random.randint(1, constants.MAX_VALUE_LEN)
            key = ""
            val = ""
            for j in range(keyLen):
                key += chr(randAscii())
            for j in range(valLen):
                val += chr(randAscii())
            if program.add(key, val) : successes += 1
        numKeys = len(program.keys())
        self.assertEqual(successes, numKeys)

if __name__ == '__main__':
    unittest.main()