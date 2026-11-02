from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask App</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(120deg, #84fab0, #8fd3f4);
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: white;
                padding: 30px;
                width: 60%;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            }

            h1 {
                color: #333;
            }

            p {
                font-size: 18px;
                color: #555;
            }

            footer {
                margin-top: 20px;
                font-size: 14px;
                color: gray;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Hello Everyone! Welcome to GitHub Actions</h1>

            <p> Hello users from <b>GitHub Actions</b></p>

            <p>Happy Learning & CI/CD Automation</p>
        </div>

        <footer>
            © 2026 | Flask + GitHub Actions Demo
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
