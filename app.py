from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Welcome to Secure Data Insights Dashboard 🔒</h2><p>Flask is running successfully!</p>"

if __name__ == "__main__":
    app.run(debug=True)

