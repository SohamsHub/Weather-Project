from concurrent.futures import ThreadPoolExecutor
from src.apis import find_place, get_current, get_daily, get_hourly
from src.shortcuts import get_pic_url, get_src, get_icons, get_arr, get_map, throw_error

def get_weather_data(place=None, headers=None):
    icons = get_icons()

    arr = get_arr()

    map = get_map()
    # find the place using the API
    with ThreadPoolExecutor() as executor:
        future_place = executor.submit(find_place, place, headers=headers)
        response = future_place.result()

    if response.status_code != 200:
        throw_error(response)

    place_data = response.json()[0]
    latitude = place_data["lat"]
    longitude = place_data["lon"]
    placename = place_data["name"]
    
    lat = float(latitude[:-1:])
    lon = float(longitude[:-1:])

    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        raise Exception("Invalid latitude or longitude values.")
    
    # get the current weather data
    with ThreadPoolExecutor() as executor:
        future_current = executor.submit(get_current, latitude, longitude, headers=headers)
        response = future_current.result()

    if response.status_code != 200:
        throw_error(response)

    weather_data = response.json()
    icon_num = weather_data["current"]["icon_num"]

    pic_url = get_pic_url(icon_num)

    # get the daily weather prediction data
    with ThreadPoolExecutor() as executor:
        future_daily = executor.submit(get_daily, latitude, longitude, headers=headers)
        response = future_daily.result()

    if response.status_code != 200:
        throw_error(response)

    prediction_data = response.json()
    temp_data = prediction_data["daily"]["data"][0]["weather"].split("_")
    predictedWeather = " ".join(temp_data).capitalize()

    # get the hourly weather data
    with ThreadPoolExecutor() as executor:
        future_hourly = executor.submit(get_hourly, latitude, longitude, headers=headers)
        response = future_hourly.result()

    if response.status_code != 200:
        throw_error(response)
    

    hour_data = response.json()

    jsonData = {"x": [], "y": []}

    for i in range(12):
        num = int(hour_data["hourly"]["data"][i]["date"][11:13:])
        if num == 24:
            data = "00 AM"
        elif num == 12:
            data = "12 PM"
        elif num > 12:
            data = str(num - 12) + " PM"
        else:
            data = str(num) + " AM"

        jsonData["x"].append(data)
        jsonData["y"].append(hour_data["hourly"]["data"][i]["temperature"])

        src = [""] * 8
        for i in range(8):
            val = prediction_data["daily"]["data"][i]["weather"]
            src[i] = get_src(val, map)

    context = {
        "latitude": lat,
        "longitude": lon,
        "weather": weather_data,
        "prediction": prediction_data,
        "icon": icons,
        "pic_urls": pic_url,
        "place": placename,
        "map": map,
        "predictedWeather": predictedWeather,
        "jsonData": jsonData,
        "arr": arr,
        "src": src,
    }

    return context