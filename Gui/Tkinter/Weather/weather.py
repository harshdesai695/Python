from tkinter.constants import INSERT
import requests, json 
import tkinter

win=tkinter.Tk()
win.title('Weather APP')
win.geometry('500x500')

fcity=tkinter.StringVar()

# Enter your API key here 
api_key = "Your Api Key"

def print_weather(result,city):
	# print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	# print("Wind speed: {} m/s".format(result['wind']['speed']))
	# print("Weather: {}".format(result['weather'][0]['main']))
	# print("Humidity: {}".format(result['main']['humidity']))
    ans=("{}'s temperature: {}°C ".format(city,result['main']['temp'])+
         "\nWind speed: {} m/s".format(result['wind']['speed'])+
         "\nWeather: {}".format(result['weather'][0]['main'])+
         "\nHumidity: {}".format(result['main']['humidity']))
    ta.delete("1.0","end")     
    ta.insert(INSERT, ans)
    ta.pack()

def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID='+api_key+'&units=metric')
	return res.json()

def Find_weather():
    try:
        fcityentry=fcity.get()
        query='q='+fcityentry
        wdata=weather_data(query)
        print_weather(wdata,fcityentry)
    except:
        ta.delete("1.0","end")     
        ta.insert(INSERT,"Cant find city ...  ")
        ta.pack()

c=tkinter.Label(win,text='Enter City: ',justify='left').pack()
c=tkinter.Entry(win,width=50,justify='left',textvariable=fcity).pack()
b=tkinter.Button(win,text="Find",command=Find_weather,).pack()
ta=tkinter.Text(win,width=50,height=25,padx=5,pady=5)
win.mainloop()
