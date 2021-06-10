import requests
import geocoder
import wikipedia


class Weather:

    def __init__(self):
        self.location = ""
        self.API = "c5849659fce58c8c0e1d20a8f9aa2edd"
        self.weather_main = ""
        self.weather_desc = ""
        self.temperature = ""
        self.maxtemp = ""
        self.mintemp = ""

    def get_today_weather(self):
        if not self.weather_main:
            json_data = self.establish_info()
            self.weather_main = json_data['weather'][0]["main"]
            self.weather_desc = json_data['weather'][0]["description"]
            self.temperature = json_data['main']['temp']
            self.maxtemp = json_data['main']['temp_max']
            self.mintemp = json_data['main']['temp_min']
        return [self.weather_main, self.weather_desc, self.temperature, self.mintemp, self.maxtemp]

    def establish_info(self):
        while True:
            g = geocoder.ip('me')
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?lat={g.latlng[0]}&lon={g.latlng[1]}&appid={self.API}&units=metric")
            if response.status_code == 200:
                return response.json()
            else:
                print("An unknown error has occurred. Trying again...")


class WikiAccess:

    def __init__(self):
        pass

    @staticmethod
    def search_pedia(term):
        resp = wikipedia.search(term)
        print(resp)

    @staticmethod
    def summary_pedia(term, sentences):
        resp = wikipedia.summary(term, sentences=sentences)
        return resp

    @staticmethod
    def get_wiki_page(term):
        resp = wikipedia.page(term)
        return resp


if __name__ == '__main__':
    print(WikiAccess.get_wiki_page("Nikola Tesla").content)
