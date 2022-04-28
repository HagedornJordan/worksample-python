from lib2to3.pgen2 import token
import constants
# Global Multi-Value Dictionary
def initDict():
  global _multiValueDict
  _multiValueDict = {}

def printNumbered(index, toPrint):
  print("%s) %s" %(index + 1, toPrint))

# keys. Returns all keys in the dictionary. Order is not guaranteed.
def keys() :
  return _multiValueDict.keys()

# commandline driver for keys.
def cmdKeys():
  allKeys = keys()
  if not allKeys:
    print(constants.KEYS_EMPTY)
  for i, key in enumerate(allKeys):
    printNumbered(i, key)

# members. Returns the collection of strings for the given key. Order is not guaranteed.
def members(key) :
  result = []
  if _multiValueDict.get(key) is not None:
    for value in _multiValueDict.get(key):
      result.append(value)
  return result

# commandline driver for members.
def cmdMembers(key):
  allMembers = members(key)
  if not allMembers:
    print(constants.ERR_KEY_NONEXISTENT_PUNC)
  else:
    for i, value in enumerate(allMembers):
      printNumbered(i, value)

# add. Takes a key, value pair and adds it to the multiValueDict. 
# Returns true if succeeds, else false
def add(key, value):
  existingValues = _multiValueDict.get(key)
  if existingValues is not None:
    if value in existingValues:
      return False
    else:
      existingValues.append(value)
      return True
  else :
    _multiValueDict[key] = [value]
    return True

# commandline driver for add.
def cmdAdd(key, value):
  added = add(key, value)
  if added:
    print(constants.ADD_SUCCESS)
  else:
    print(constants.ERR_MEMBER_EXISTS)

# remove. Takes a key, value par and removes it from the multiValueDict.
# returns 0 on success, 1 if member nonexistent, 2 if key nonexistent
def remove(key, value):
  existingValues = _multiValueDict.get(key)
  if existingValues is not None:
    if value in existingValues:
      existingValues.remove(value)
      if not existingValues:
        _multiValueDict.pop(key)
      return 0
    else:
      return 1
  else:
    return 2

# commandline driver for remove.
def cmdRemove(key, value):
  result = remove(key, value)
  match(result):
    case 0:
      print(constants.REMOVE_SUCCESS)
    case 1:
      print(constants.ERR_MEMBER_NONEXISTENT)
    case 2:
      print(constants.ERR_KEY_NONEXISTENT)


# removeAll. Remove all members for a key and removes the key from the dictionary. Returns an error if the key does not exist.
def removeAll(key):
  if key in _multiValueDict:
    _multiValueDict.pop(key)
    return True
  else:
    return False

# commandline driver for removeall.
def cmdRemoveAll(key):
  result = removeAll(key)
  if (result):
    print(constants.REMOVE_SUCCESS)
  else:
    print(constants.ERR_KEY_NONEXISTENT)

# Removes all keys and all members from the dictionary.
def clear():
  initDict()

# commandline driver clear.
def cmdClear():
  clear()
  print(constants.CLEAR_SUCCESS)


# keyExists. Returns whether a key exists or not.
def keyExists(key):
  if key in _multiValueDict:
    return True
  return False

# commandline driver for keyExists.
def cmdKeyExsits(key):
  if keyExists(key):
    print(constants.EXISTS_TRUE)
  else:
    print(constants.EXISTS_FALSE)

# memberexists. Returns whether a member exists within a key. Returns false if the key does not exist.
def memberExists(key, value):
  existingValues = _multiValueDict.get(key)
  if existingValues is not None:
    if value in existingValues:
      return True
  return False

# commandline driver for memberExists.
def cmdMemberExsits(key, value):
  if memberExists(key, value):
    print(constants.EXISTS_TRUE)
  else:
    print(constants.EXISTS_FALSE)
  
# allMembers. Returns all the members in the dictionary. Returns nothing if there are none. Order is not guaranteed.
def allMembers():
  result = []
  for key in _multiValueDict:
    for value in _multiValueDict.get(key):
      result.append(value)
  return result

# commandline driver for allMembers.
def cmdAllMembers():
  result = allMembers()
  if not result:
    print(constants.ALLMEMBERS_EMPTY)
  else:
    for i, value in enumerate(result):
      printNumbered(i, value)

  
# items. Returns all keys in the dictionary and all of their members. Returns nothing if there are none. Order is not guaranteed.
def items():
  result = []
  if not _multiValueDict:
    return result
  else:
    for key in _multiValueDict:
      for value in _multiValueDict.get(key):
        result.append(key + ": " + value)
  return result

#commandline driver for items.
def cmdItems():
  result = items()
  if not result:
    print(constants.ALLMEMBERS_EMPTY)
  else:
    for i, value in enumerate(result):
      printNumbered(i, value)

# helper to print invalid command.
def invalidCommand(command):
  print("Invalid Command entered: %s" %(command))

# helper to print invalid number of args.
def invalidArgumentCount(command, arguments, needed):
  print ("Invalid number of args for command %s. Expected (%s), got (%s)." %(command, needed, len(arguments)))

# validate input. Used to check user input. In the future, we could perform more validations (sanitize user input)
def validateInput(command, arguments):
  if command not in constants.ALL_CMDS: 
    invalidCommand(command)
    return False
  expected = 0
  match(command):
    case constants.CMD_ADD | constants.CMD_REMOVE | constants.CMD_MEMBEREXISTS:
      expected = 2
    case constants.CMD_KEYEXISTS | constants.CMD_MEMBERS | constants.CMD_REMOVEALL | constants.CMD_KEYEXISTS:
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
  if validateInput(command, arguments):
    match command:
      case constants.CMD_KEYS:
        cmdKeys()
      case constants.CMD_MEMBERS:
        cmdMembers(arguments[0])
      case constants.CMD_ADD:
        cmdAdd(arguments[0], arguments[1])
      case constants.CMD_REMOVE:
        cmdRemove(arguments[0], arguments[1])
      case constants.CMD_REMOVEALL:
        cmdRemoveAll(arguments[0])
      case constants.CMD_CLEAR:
        cmdClear()
      case constants.CMD_KEYEXISTS:
        cmdKeyExsits(arguments[0])
      case constants.CMD_MEMBEREXISTS:
        cmdMemberExsits(arguments[0], arguments[1])
      case constants.CMD_ALLMEMBERS:
        cmdAllMembers()
      case constants.CMD_ITEMS:
        cmdItems()
      case _:
        invalidCommand(command)

if __name__ == '__main__':
  initDict()
  while True:
    userInput = input("> ")
    processInput(userInput)