from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Route for T-shirts page
@app.route('/tshirts')
def tshirts():
    return render_template('tshirts.html')

# Route for Bags page
@app.route('/bags')
def bags():
    return render_template('bags.html')

# Route for Cups page
@app.route('/cups')
def cups():
    return render_template('cups.html')

if __name__ == "__main__":
    app.run()
