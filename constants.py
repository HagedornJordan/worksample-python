# Commands
CMD_KEYS = "KEYS"
CMD_MEMBERS = "MEMBERS"
CMD_ADD = "ADD"
CMD_REMOVE = "REMOVE"
CMD_REMOVEALL = "REMOVEALL"
CMD_CLEAR = "CLEAR"
CMD_KEYEXISTS = "KEYEXISTS"
CMD_MEMBEREXISTS = "MEMBEREXISTS"
CMD_ALLMEMBERS = "ALLMEMBERS"
CMD_ITEMS = "ITEMS"

ALL_CMDS = [CMD_KEYS, CMD_MEMBERS, CMD_ADD, CMD_REMOVE, CMD_REMOVEALL, CMD_CLEAR, CMD_KEYEXISTS, CMD_MEMBEREXISTS, CMD_ALLMEMBERS, CMD_ITEMS]

# Command feedback
ADD_SUCCESS = ") Added"
REMOVE_SUCCESS = ") Removed"
CLEAR_SUCCESS = ") Cleared"
KEYS_EMPTY = ") empty set"
ALLMEMBERS_EMPTY = "(empty set)"
EXISTS_TRUE = ") true"
EXISTS_FALSE = ") false"



# Error strings
ERR = ") ERROR, "
ERR_KEY_NONEXISTENT = ERR + "key does not exist"
ERR_KEY_NONEXISTENT_PUNC = ERR_KEY_NONEXISTENT + "."
ERR_MEMBER_EXISTS = ERR + "member already exists for key"
ERR_MEMBER_NONEXISTENT = ERR + "member does not exist"
