import weather_view
import weather_model

def GetChoice():
	'''Get choice from user:
		N/n - New Search
		Q/q - Quit			''' 
	choice=input(weather_view.StartView())
	# 1. weather_view.StartView()
	if choice=='q' or choice== 'Q':
		# 2. weather_view.EndView()
		weather_view.EndView()
	elif choice=='n' or choice=='N':
		# 3. GetLocation() 
		search=GetLocation()
	else:
		weather_view.InvalidEntry()
		# 4. weather_view.InvalidEntry()
		GetChoice()

def GetLocation():
	location=input(weather_view.LocationView())
	# 5. weather_view.LocationView()
	search=weather_model.LocationSearch(location)
	# 6. weather_model.LocationSearch(location)
	if search[0]=='Success':
		weather_view.LocationSuccess([search[1], search[2]])
		# 7. weather_view.LocationSuccess()
		weather_dict = weather_model.WeatherDetails(search[1], search[2], search[3])
		# 8. weather_model.WeatherDetails()
		weather_view.ViewWeather(search[1], search[2], weather_dict)
		GetChoice()
	else:
		weather_view.LocationFailed(location)
		GetChoice()

if __name__== '__main__':
	GetChoice()