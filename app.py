from flask import Flask, render_template, request

app = Flask(__name__)

def safe_eval(expr: str) -> str:
    # allow only safe characters
    allowed = set("0123456789+-*/.() ")
    if any(ch not in allowed for ch in expr):
        return "Error"
    try:
        return str(eval(expr))
    except:
        return "Error"

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")

        if "clear" in request.form:
            expression = ""
            result = ""
        elif "equals" in request.form:
            result = safe_eval(expression)
        else:
            # button pressed → append value
            value = request.form.get("value", "")
            expression += value

    return render_template("index.html", expression=expression, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)