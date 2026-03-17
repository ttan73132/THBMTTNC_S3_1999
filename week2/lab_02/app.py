from flask import Flask, render_template, request
from ex01.cipher.caesar.caesar_cipher import CaesarCipher
from ex01.cipher.railfence.railfence_cipher import RailFenceCipher
from ex01.cipher.playfair.playfair_cipher import PlayFairCipher


app = Flask(__name__)

# MAIN ROUTE 
@app.route("/")
def home():
    return render_template('index.html')
# CAESAR
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br>/key: {key}<br>/encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br>/key: {key}<br>/decrypted text: {decrypted_text}"

# PLAYFAIR 
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
        data = request.json  
        key = data.get('key', '') 
        playfair_cipher = PlayFairCipher()
        playfair_matrix = playfair_cipher.create_playfair_matrix(key) 
        return jsonify({"playfair_matrix": playfair_matrix})

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, playfair_matrix)
    return f"text: {text}<br>/key: {key}<br>/encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, playfair_matrix)
    return f"text: {text}<br>/key: {key}<br>/decrypted text: {decrypted_text}"


#  RAILFENCE 
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text: {text}<br>/key: {key}<br>/encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br>/key: {key}<br>/decrypted text: {decrypted_text}"

#  MAIN FUNCTION 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)