from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the webpage
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <title>Factorial Calculator</title>
</head>
<body>
  <h2>Calculate Factorial</h2>
  <form method="POST">
    <label for="number">Enter a number:</label>
    <input type="text" id="number" name="number">
    <button type="submit">Calculate</button>
  </form>
  {% if result is not none %}
  <h3>Result: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        number = int(request.form['number'])
        result = factorial(number)
        return render_template_string(HTML_TEMPLATE, result=result)
    return render_template_string(HTML_TEMPLATE, result=None)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

