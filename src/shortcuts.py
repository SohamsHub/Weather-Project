def get_pic_url(icon_num):
    pic_icons = [
        "/static/images/sunny.jpeg",
        "/static/images/rain.jpeg",
        "/static/images/cloud.jpeg",
        "/static/images/snowy.jpeg",
        "/static/images/fog.jpeg",
        "/static/images/cloud-sun.jpeg",
        "/static/images/thunder.jpeg",
    ]

    sunny = [2, 3, 26, 27]
    rain = [10, 11, 12, 13, 25, 32, 23, 24, 36]
    cloudy = [6, 7, 8, 30, 31]
    snowy = [16, 17, 18, 19, 20, 21, 22, 35, 34]
    fog = [9, 1, 0]
    thunder = [14, 15, 33]
    cloudy_sunny = [28, 4, 5, 29]

    if icon_num in rain:
        pic_url = pic_icons[1]
    elif icon_num in cloudy:
        pic_url = pic_icons[2]
    elif icon_num in snowy:
        pic_url = pic_icons[3]
    elif icon_num in fog:
        pic_url = pic_icons[4]
    elif icon_num in cloudy_sunny:
        pic_url = pic_icons[5]
    elif icon_num in thunder:
        pic_url = pic_icons[6]
    else:
        pic_url = pic_icons[0]

    return pic_url


def get_src(data, map):
    if data in map:
        src_info = map[data]
    else:
        if "rain" in data:
            src_info = "/static/icons/animated/rainy-7.svg"
        elif "snow" in data:
            src_info = "/static/icons/animated/snowy-4.svg"
        elif "sun" in data:
            src_info = "/static/icons/animated/weather.svg"
        elif "cloud" in data:
            src_info = "/static/icons/animated/cloudy-day-2.svg"
        elif "thunder" in data or "storm" in data:
            src_info = "/static/icons/animated/thunder.svg"
        else:
            src_info = "/static/icons/animated/not_available.jpeg"

    return src_info


def get_icons():
    icons = [
        "/static/icons/animated/not_available.jpeg",
        "/static/icons/animated/not_available.jpeg",
        "/static/icons/animated/day.svg",
        "/static/icons/animated/cloudy-day-1.svg",
        "/static/icons/animated/cloudy-day-2.svg",
        "/static/icons/animated/cloudy-day-3.svg",
        "/static/icons/animated/cloudy.svg",
        "/static/icons/animated/cloudy.svg",
        "/static/icons/animated/cloudy-day-3.svg",
        "/static/icons/animated/fog.jpeg",
        "/static/icons/animated/rainy-4.svg",
        "/static/icons/animated/rainy-5.svg",
        "/static/icons/animated/rainy-1.svg",
        "/static/icons/animated/rainy-6.svg",
        "/static/icons/animated/thunder.svg",
        "/static/icons/animated/thunder.svg",
        "/static/icons/animated/snowy-2.svg",
        "/static/icons/animated/snowy-4.svg",
        "/static/icons/animated/snowy-1.svg",
        "/static/icons/animated/snowy-6.svg",
        "/static/icons/animated/rainy-7.svg",
        "/static/icons/animated/rainy-7.svg",
        "/static/icons/animated/rainy-7.svg",
        "/static/icons/animated/weather.svg",
        "/static/icons/animated/weather.svg",
        "/static/icons/animated/rainy-7.svg",
        "/static/icons/animated/day.svg",
        "/static/icons/animated/cloudy-day-1.svg",
        "/static/icons/animated/cloudy-day-2.svg",
        "/static/icons/animated/cloudy-day-3.svg",
        "/static/icons/animated/cloudy.svg",
        "/static/icons/animated/rainy-1.svg",
        "/static/icons/animated/rainy-6.svg",
        "/static/icons/animated/thunder.svg",
        "/static/icons/animated/snowy-6.svg",
        "/static/icons/animated/weather.svg",
        "/static/icons/animated/weather.svg",
    ]

    return icons


def get_arr():
    arr = [
        "not_available",
        "not_available",
        "sunny",
        "mostly_sunny",
        "partly_sunny",
        "mostly_cloudy",
        "cloudy",
        "overcast",
        "overcast_with_low_clouds",
        "fog",
        "light_rain",
        "rain",
        "possible_rain",
        "rain_shower",
        "thunderstorm",
        "local_thunderstorms",
        "light_snow",
        "snow",
        "possible_snow",
        "snow_shower",
        "rain_and_snow",
        "possible_rain_and_snow",
        "rain_and_snow",
        "freezing_rain",
        "possible_freezing_rain",
        "hail",
        "clear_night",
        "mostly_clear_night",
        "partly_clear_night",
        "mostly_cloudy_night",
        "cloudy_night",
        "overcast_with_low_clouds_night",
        "rain_shower_night",
        "local_thunderstorms_night",
        "snow_shower_night",
        "rain_and_snow_night",
        "possible_freezing_rain_night",
    ]

    return arr


def get_map():
    map = {
        "not_available": "/static/icons/animated/not_available.jpeg",
        "sunny": "/static/icons/animated/day.svg",
        "mostly_sunny": "/static/icons/animated/cloudy-day-1.svg",
        "partly_sunny": "/static/icons/animated/cloudy-day-2.svg",
        "mostly_cloudy": "/static/icons/animated/cloudy-day-3.svg",
        "cloudy": "/static/icons/animated/cloudy.svg",
        "overcast": "/static/icons/animated/cloudy.svg",
        "overcast_with_low_clouds": "/static/icons/animated/cloudy-day-3.svg",
        "fog": "/static/icons/animated/fog.jpeg",
        "light_rain": "/static/icons/animated/rainy-4.svg",
        "rain": "/static/icons/animated/rainy-5.svg",
        "possible_rain": "/static/icons/animated/rainy-1.svg",
        "rain_shower": "/static/icons/animated/rainy-6.svg",
        "thunderstorm": "/static/icons/animated/thunder.svg",
        "local_thunderstorms": "/static/icons/animated/thunder.svg",
        "light_snow": "/static/icons/animated/snowy-2.svg",
        "snow": "/static/icons/animated/snowy-4.svg",
        "possible_snow": "/static/icons/animated/snowy-1.svg",
        "snow_shower": "/static/icons/animated/snowy-6.svg",
        "rain_and_snow": "/static/icons/animated/rainy-7.svg",
        "possible_rain_and_snow": "/static/icons/animated/rainy-7.svg",
        "freezing_rain": "/static/icons/animated/weather.svg",
        "possible_freezing_rain": "/static/icons/animated/weather.svg",
        "hail": "/static/icons/animated/rainy-7.svg",
        "clear_night": "/static/icons/animated/day.svg",
        "mostly_clear_night": "/static/icons/animated/cloudy-day-1.svg",
        "partly_clear_night": "/static/icons/animated/cloudy-day-2.svg",
        "mostly_cloudy_night": "/static/icons/animated/cloudy-day-3.svg",
        "cloudy_night": "/static/icons/animated/cloudy.svg",
        "overcast_with_low_clouds_night": "/static/icons/animated/rainy-1.svg",
        "rain_shower_night": "/static/icons/animated/rainy-6.svg",
        "local_thunderstorms_night": "/static/icons/animated/thunder.svg",
        "snow_shower_night": "/static/icons/animated/snowy-6.svg",
        "rain_and_snow_night": "/static/icons/animated/weather.svg",
        "possible_freezing_rain_night": "/static/icons/animated/weather.svg",
    }

    return map

def throw_error(response):
    raise Exception(
        f"Error fetching current weather data: {response.status_code} - {response.text}"
    )