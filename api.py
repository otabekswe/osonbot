def check_token(token: str) -> bool:
    if any(char.isspace() for char in token):
        return False
    
    left, sep, right = token.partition(':')
    if len(left) < 3 or (not sep) or (not left.isdigit()):
        return False
    
    return True
    

print(check_token('5338589332:AAFK6v4qSIJde5zyIjMA-WY3xnfGxDpW2ec'))

class Methods:
    getMe = 'getMe'
    logOut = 'logOut' # soon
    sendMessage = 'sendMessage' # soon
    forwardMessage = 'forwardMessage' # soon
    copyMessage = 'copyMessage'
    sendPhoto = 'sendPhoto' # soon
    sendVideo = 'sendVideo' # soon
    sendAnimation = 'sendAnimation' # soon
    sendAudio = 'sendAudio' # soon
    sendDocument = 'sendDocument' # soon
    sendVoice = 'sendVoice' # soon
    sendVideoNote = 'sendVideoNote' # soon
    sendMediaGroup = 'sendMediaGroup' # soon
    sendLocation = 'sendLocation' # soon
    sendContact = 'sendContact' # soon
    sendPoll = 'sendPoll' # soon
    sendDiece = 'sendDiece' # soon
    sendChatAction = 'sendChatAction' # soon
    getUserProfilePhoto = 'getUserProfilePhoto' # soon
    getFile = 'getFile' # soon
    banChatMember = 'banChatMember' # soon
    unBanChatMember = 'unBanChatMember' # soon
    restrictChatMember = 'restrictChatMember' # soon
    promoteChatMember = 'promoteChatMember' # soon
    pinChatMessage = 'pinChatMessage' # soon
    getChat = 'getChat' # soon
    getChatAdmin = 'getChatAdmin' # soon
    getChatMemberCount = 'getChatMemberCount' # soon