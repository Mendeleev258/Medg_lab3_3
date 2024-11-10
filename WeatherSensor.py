class GeoCoordinate:
    def __init__(self, degrees: int = 0, minutes: int = 0, seconds: int = 0, mseconds: int = 0):
        self.__degrees = degrees # 0 - 360
        self.__minutes = minutes # 0 - 60
        self.__seconds = seconds # 0 - 60
        self.__mseconds = mseconds # 0 - 1000
    
    @property
    def degrees(self) -> int:
        return self.__degrees
    @property
    def minutes(self) -> int:
        return self.__minutes
    @property
    def seconds(self) -> int:
        return self.__seconds
    @property
    def mseconds(self) -> int:
        return self.__mseconds

    def __str__(self):
        return f'{self.__degrees}.{self.__minutes}.{self.__seconds}.{self.__mseconds}'

    
def temperature_decorator(method):
    def wrapper(self):
        temperature = method(self)
        return f'{temperature}°'
    return wrapper


class WeatherSensor:
    def __init__(self, longitude: GeoCoordinate = None, latitude: GeoCoordinate = None, id: str = '', temperature: float = 0.0, wetness: float = 0.0):
        self.__longitude = longitude
        self.__latitude = latitude
        self.__id = id
        self.__temperature = temperature
        self.__wetness = wetness
    
    @property
    def longitude(self) -> str:
        return self.__longitude
    
    @property
    def latitude(self) -> str:
        return self.__latitude
    
    @property
    def id(self) -> int:
        return self.__id
   
    @property
    @temperature_decorator
    def temperature(self) -> float:
        return self.__temperature
    
    @property
    def wetness(self) -> float:
        return self.__wetness
    
    def __str__(self):
        return (f'Longitude: {self.__longitude}\n'
                f'Latitude: {self.__latitude}\n'
                f'ID: {self.__id}\n'
                f'Temperature: {self.temperature}\n'
                f'Wetness: {self.__wetness}%')
    
    def is_empty(self) -> bool:
        if (self.__longitude is None or 
            self.__latitude is None or 
            self.__id is None or 
            self.__temperature is None or 
            self.__wetness is None):
            return True
        return False