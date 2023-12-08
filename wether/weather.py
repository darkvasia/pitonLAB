import csv

class WeatherData:
    def __init__(self, date, temperature, humidity, precipitation):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
        self.precipitation = precipitation

    def __str__(self):
        return f"Date: {self.date}, Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Precipitation: {self.precipitation}mm"

class WeatherAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.weather_data = []

    def load_data(self):
        try:
            with open(self.filepath, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    if row:
                        weather = WeatherData(date=row[0], temperature=float(row[1]), humidity=float(row[2]), precipitation=float(row[3]))
                        self.weather_data.append(weather)
        except FileNotFoundError:
            print(f"File not found: {self.filepath}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_data(self):
        for data in self.weather_data:
            print(data)

# Usage
analyzer = WeatherAnalyzer('path_to_your_csv.csv')
analyzer.load_data()
analyzer.display_data()
