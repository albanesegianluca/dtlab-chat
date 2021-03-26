# Questo modulo utilizza Flask per realizzare un web server. L'applicazione può essere eseguita in vari modi
# FLASK_APP=server.py FLASK_ENV=development flask run
# python server.py se aggiungiamo a questo file app.run()

from flask import Flask, request, jsonify
import results
import user
import message

# viene creata l'applicazione con il nome del modulo corrente.
app = Flask(__name__)

# getErrorCode è una funzione di utilità che mappa i valori ritornati dal modulo user con quelli del
# protocollo HTTP in caso di errore. 
# 404 - Not Found: una risorsa non è stata trovata sul server;
# 403 - Forbidden: accesso negato;
# 409 - Conflict: è violato un vincolo di unicità. Ad esempio, esiste già un utente con la stessa mail registrata;
# Come ultima spiaggia è buona norma ritornare "500 - Internal Server Error" per indicare che qualcosa è andato storto
def getErrorCode(result: results.Result) -> int:
    if result is results.Result.NOT_FOUND:
        code = 404
    elif result is results.Result.EMPTY_MESSAGE:
        code = 404
    elif result is results.Result.NOT_AUTHORIZED:
        code = 403
    elif result is results.Result.DUPLICATED:
        code = 409
    else:
        code = 500

    return code

@app.route('/user', methods=['POST'])
def createUser():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    email = data['email']
    password = data['password']
    
    result, u = user.SaveUser(name, surname, email, password)

    if result is not results.Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return u, 201

@app.route('/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    result, u = user.Login(email, password)

    if result is not results.Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return u, 200

@app.route('/inbox', methods=['POST'])
def SaveMessage():
    data = request.get_json()
    emailSender = data['email']
    emailRecipient = data['recipient']
    messageToSend = data['message']

    result = message.SaveMessage(emailSender, emailRecipient, messageToSend)

    if result is not results.Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return '', 201

@app.route('/inbox/<string:userId>', methods=['GET'])
def GetMessage(userId):
    result, m = message.GetMessage(userId)

    if result is not results.Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return jsonify(m), 200

@app.route('/user/<string:userId>', methods=['DELETE'])
def DeleteUser(userId):
    result = user.CheckAuthUser(userId, request.headers["Authorization"])

    if result is not results.Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return '', 204

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
