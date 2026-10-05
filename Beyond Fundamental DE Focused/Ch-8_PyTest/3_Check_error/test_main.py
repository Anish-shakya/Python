from main import weather
import pytest
# Test Cases for weather_check method

def test_weather_check():
    w = weather()
    
    assert w.weather_check(-5) == "It's freezing outside!"
    assert w.weather_check(10) == "It's a bit chilly"
    assert w.weather_check(20) == "The weather is pleasant."
    assert w.weather_check(30) == "It's hot outside!"

## Test Case for rain_chance method

def test_rain_chance_check():
    w = weather()
    
    assert w.rain_check(0.9) == "It's likely to rain. Don't forget yout umbrella"
    assert w.rain_check(0.7) == "There's a chance of rain. You might want to carry umbrella"
    assert w.rain_check(0.1) == "It's unlikely to rain today"

def test_divide():
    
    w=weather()
    
    assert w.divide(10,2) == 5
    assert w.divide(9,3) == 3

    with pytest.raises(ValueError,match="Cannot Divide By Zero!"):
        w.divide(5,0)