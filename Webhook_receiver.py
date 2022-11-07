from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        a = request.json
        b = a["content"]
        if b == "buy":
            print("compra")
        elif b == "sell": 
            print("venta")   
        else:
            print("no paso nada")     
        return 'success', 200
    
    else:
        abort(400)

if __name__ == '__main__':
    app.run()