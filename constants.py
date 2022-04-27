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

# Command feedback
ADD_SUCCESS = ") Added"
REMOVE_SUCCESS = ") Removed"
CLEAR_SUCCESS = ") Cleared"
KEYS_EMPTY = ") empty set"


# Error strings
ERR = ") ERROR, "
ERR_KEY_NONEXISTENT = ERR + "key does not exist"
ERR_KEY_NONEXISTENT_PUNC = ERR + ERR_KEY_NONEXISTENT + "."
ERR_MEMBER_EXISTS = ERR + "member already exists for key"
ERR_MEMBER_NONEXISTENT = ERR + "member does not exist"
