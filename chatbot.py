import requests, random, datetime
from time import sleep
def get_weather():
    key = 'c973e051a52d4f1122c7a0f9eff64fe4'
    city = input('What is the name of the city you want to get the weather of?')
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}'
    response = requests.get(url)
    x = response.json()
    if x['cod'] != '404':
        y = x['main']
        temp = y['temp']
        temp = int((1.8 * (temp - 273)) + 32)
        feelslike = y['feels_like']
        feelslike = int((1.8 * (feelslike - 273)) + 32)
        maximum = y['temp_max']
        maximum = int((1.8 * (maximum - 273)) + 32)
        minimum = y['temp_min']
        minimum = int((1.8 * (minimum - 273)) + 32)
        humidity = y['humidity']
        z = x['weather']
        description = z[0]['description']
        print(f'Description : {description}')
        print(f'Temperature : {temp}°F')
        print(f'Feels Like: {feelslike}°F')
        print(f'High Today: {maximum}°F')
        print(f'Low Today: {minimum}°F')
        print(f'Humidity : {humidity}%')
    else:
        print('The city was not found.')
def tell_a_joke():
    number_of_jokes = 3
    joke_num = random.randint(1, number_of_jokes)
    if joke_num == 1:
        print('What’s the best thing about Switzerland?')
        sleep(5)
        print('I don’t know, but the flag is a big plus.')
    elif joke_num == 2:
        print('I invented a new word!')
        sleep(5)
        print('Plagiarism!')
    elif joke_num == 3:
        print('Do you know why we tell actors to "break a leg"?')
        sleep(5)
        print('Because every play has a cast.')
name = 'Atul'
birthday = '04/16/2010'
day = datetime.datetime.now()
day = day.strftime('%x')
if day[:5] == birthday[:5]:
    say_happy_b_day = True
else:
    say_happy_b_day = False
while True:
    if say_happy_b_day:
        print('🎉🥳Happy Birthday!🎉🥳')
        say_happy_b_day = False
    user_says = input().lower()
    user_says = user_says.strip()
    if user_says == 'what is the weather' or user_says == 'what is the weather?' or user_says == 'what is the weather outside' or user_says == 'what is the weather outside?':
        get_weather()
    elif user_says == 'tell me a joke' or user_says == 'gimme a joke' or user_says == 'give me a joke' or user_says == 'please tell me a joke':
        tell_a_joke()
    elif user_says == 'hello' or user_says == 'hello!' or user_says == 'hi' or user_says == 'hi!' or user_says == 'hey' or user_says == 'hey!':
        print('Hello!')