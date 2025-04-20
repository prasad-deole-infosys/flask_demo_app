from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Flask app on Google Cloud Run!"

@app.route('/hello')
def hello():
    html = """
    <html>
      <head><title>Hello</title></head>
      <body>
        <h1>Hello from Flask on Cloud Run!</h1>
      </body>
    </html>
    """
@app.route('/new-routing')
def new_routing():
    html = """
    <html>
      <head><title>New Routing</title></head>
      <body>
        <h1>Hello from Flask on Cloud Run!<br>Welcome to the New Routing!!!!</h1>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
