import time
import results
import user

messages = []
# message format
#message = {
#    senderId = "mittente",
#    recipientId = "destinatario",
#    message = "Messaggio"
#    timestamp = "Timestamp invio messaggio"
#}

def GetMessage(userId):
    messagesList = []

    if(user.findUserByID(userId) == None):
        return results.Result.NOT_FOUND, messagesList

    for message in messages:
        if(str(message["recipientId"]) == userId): # I have a message!
            print("Message found")
            messagesList.append(message)

    return results.Result.OK, messagesList

def SaveMessage(emailSender, emailRecipient, m):
    if(user.findUserByEmail(emailSender) is None):
        return results.Result.NOT_FOUND
    else:
        senderId = user.findUserByEmail(emailSender)['id']

    if(user.findUserByEmail(emailRecipient) is None):
        return results.Result.NOT_FOUND
    else:
        recipientId = user.findUserByEmail(emailRecipient)['id']

    if(len(m) <= 0):
        return results.Result.EMPTY_MESSAGE

    ts = time.time()

    if(len(messages) <= 0):
        mId = 1 # The first message will have 1 as ID
    else:
        mId = len(messages) + 1 # Increment the messageId value by 1

    message = {
        'messageId': mId,
        'senderId': senderId,
        'recipientId': recipientId,
        'message': m,
        'timestamp': ts
    }

    messages.append(message.copy())
    return results.Result.OK
