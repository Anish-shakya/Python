
from main import weather_check
import pytest
## Test Cases for weather_check function

@pytest.mark.parametrize("temp,expected",[
    (-5,"It's freezing outside!"),
    (10,"It's a bit chilly"),
    (20,"The weather is pleasant."),
    (30,"It's hot outside!"),
])
def test_weather_check(temp,expected):
    assert weather_check(temp)==expected
 
    
if __name__ =="__main__": ## indication that only run this function when it is run from this file
    test_weather_check()