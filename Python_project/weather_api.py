import requests

def get_weather():
	# Have the user input a zip code
	zip_code: int = input("Please input Zipcode: ")
	api_key: str = "RIGHT HERE" '''insert your API key from the opeanweathermap.org'''
	
	'''creating a variable called response to use the openweathermap.org current weather API, I also edited the call for the API to include &units=imperial to give fahrenheit
	
	when the user inputs zipcode it will plug it into the API 
	along with the api key.'''
	
	response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units=imperial")

	#if the API give a successful query proceed to if https:\\ returns 200 for a successful query if 404 or 401 ect will default to error
	if response.status_code == 200:
		#data for the API is in json invoking api data to return specified fields
		data: float = response.json()
		#using data.get to access values in a dictory to allow me to specify if it cannot return a result and to give an empty dictionary {}. 
		#it attempts to get a value assosiated to the key '1h' which is in the API instructions requirement to display mm of rain. if it does not have a value it will return 0.
		rain: float = data.get('rain', {}).get('1h', 0)
		snow: float = data.get('snow',{}).get('1h',0)
		wind: float = data['wind']['speed']
		temperature: float = data['main']['temp']
		return (f"The weather in {data['name']} is {temperature}°F.\n"
		f"in the past hour it has rained: {rain}mm in the past hour.\n" 
		f"it has snowed: {snow}mm in the past hour.\n"
		f"Current wind speed is {wind} miles/hr.")
	#otherwise will give an error
	else:
		return "Failed to get the weather data."

if __name__ == '__main__':
    get_weather()