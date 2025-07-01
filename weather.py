from flask import Flask, render_template, request
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import os
from src.utility import get_weather_data

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def get_weather():
    try:
        if request.method == "POST":
            place = request.form.get("place")
        else:
            place = request.args.get("place")

        if not place:
            return render_template("weather.html", weather=None)

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_URL,
        }
        
        with ThreadPoolExecutor() as executor:
            future = executor.submit(get_weather_data, place=place, headers=headers)
            context = future.result()

        return render_template("weather.html", **context)

    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template("weather.html", weather=None)


if __name__ == "__main__":
    app.run(debug=True)