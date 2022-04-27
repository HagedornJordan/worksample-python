from lib2to3.pgen2 import token
import constants

# Global Multi-Value Dictionary
_multiValueDict = {}

#stub - used to structure project initially.
def stub() : 
  print("TODO")

# keys. Returns all keys in the dictionary. Order is not guaranteed.
def keys() :
  stub()

# members. Returns the collection of strings for the given key. Order is not guaranteed.
def members() :
  stub()

# add. Takes a key, value pair and adds it to the multiValueDict.
def add(key, value):
  stub()

# remove. Takes a key, value par and removes it from the multiValueDict.
def remove(key, value):
  stub()

# removeAll. Remove all members for a key and removes the key from the dictionary. Returns an error if the key does not exist.
def removeAll():
  stub()

# Removes all keys and all members from the dictionary.
def clear():
  stub()

# keyExists. Returns whether a key exists or not.
def keyExists():
  stub()

# memberexists. Returns whether a member exists within a key. Returns false if the key does not exist.
def memberExists():
  stub()
  
# allMembers. Returns all the members in the dictionary. Returns nothing if there are none. Order is not guaranteed.
def allMembers():
  stub()

# items. Returns all keys in the dictionary and all of their members. Returns nothing if there are none. Order is not guaranteed.
def items():
  stub()

def invalidCommand(command):
  print("Invalid Command entered: %s" %(command))

def invalidArgumentCount(command, arguments, needed):
  print ("Invalid number of args for command %s. Expected (%s), got (%s)." %(command, needed, len(arguments)))

# validate arguments. Used to check number of arguments matches what is expected. In the future, we could perform more validations (sanitize user input)
def validateArguments(command, arguments):
  expected = 0
  match(command):
    case constants.CMD_ADD | constants.CMD_REMOVE | constants.CMD_MEMBEREXISTS:
      expected = 2
    case constants.CMD_KEYEXISTS:
      expected = 1
  if len(arguments) != expected:
    invalidArgumentCount(command, arguments, expected)
    return False
  return True
  
# Process Input.
def processInput(userInput):
  tokenized = userInput.split(' ')
  command = tokenized[0]
  tokenized.remove(command)
  arguments = tokenized
  if validateArguments(command, arguments):
    match command:
      case constants.CMD_KEYS:
        keys()
      case constants.CMD_MEMBERS:
        members()
      case constants.CMD_ADD:
        add(arguments[0], arguments[1])
      case constants.CMD_REMOVE:
        remove(arguments[0], arguments[1])
      case constants.CMD_REMOVEALL:
        removeAll()
      case constants.CMD_CLEAR:
        clear()
      case constants.CMD_KEYEXISTS:
        keyExists(arguments[0])
      case constants.CMD_MEMBEREXISTS:
        memberExists(arguments[0], arguments[1])
      case constants.CMD_ALLMEMBERS:
        allMembers()
      case _:
        invalidCommand(command)

if __name__ == '__main__':
  while True:
    userInput = input("> ")
    processInput(userInput)