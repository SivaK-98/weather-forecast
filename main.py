from flask import Flask, render_template, request, jsonify
import weather

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/check", methods=['POST', 'GET'])
def check():
    if request.method == "POST":
        place = request.form.get("place")
        request_type = request.form.get("type")
        result = weather.get_weather(place, request_type)
        print("Result: ", result)
        return jsonify(result[1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
