import requests
import os
import gtts
from playsound import playsound
import time
import random
import webbrowser
import pyautogui




api_key = '8bd715a3be20c63f2c740ada9426abb7'
city = 'Lumberton'

# Converts kelvin to farenheit
def k_to_f(kelvin):

    celcius = kelvin - 273.15
    farenheit = celcius * (9/5) + 32
    return farenheit


url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=' + api_key
response = requests.get(url).json()

#converts kelivn temp to farenheit
temp_kelvin = response['main']['temp']
temp_farenheit = int(k_to_f(temp_kelvin))

#converts the feels like temp from kelvin to farenheit
feels_like_kelvin = response['main']['feels_like']
feels_like_farenheit = int(k_to_f(feels_like_kelvin))

#rainy, clear skys, cloudy, etc...
skys = response['weather'][0]['description']

hot_flavor = ["spicy", "sweat inducing", "blazing", "scorching", "sweltering", "inhumane", "brutal", "uninhabitable", "pityless", "inconsiderate", "dastardly", "chaffing", "painful"]

warm_flavor = ["acceptional", "mild", "tender", "toasty", "merciful", "balmy", "temprate", "clement", "tame", "zesty"]

just_right_flavor = ["nice", "perfect", "beautiful", "fantastic", "delightful", "succulent", "juicy", "tepid", "room temprate", "breedable", "blissful", "euphoric"]

cold_flavor = ["chilly", "crisp", "shivery", "frosty", "nippy", "fragile", "chomping", "corroding", "etching", "tart"]

freezing_flavor = ["freezing", "bitter", "snowy", "ball shriveling", "cock chilling", "biting", "terminal", "raw", "glacial", "penatrating"]




if temp_farenheit > 80:
    temp_flavor_text = random.choice(hot_flavor)
    temp_desc = "Looks like it might be pretty hot with"
elif temp_farenheit in range(70,80):
    temp_flavor_text = random.choice(warm_flavor)
    temp_desc = "Looks like it might be warm today with"
elif temp_farenheit in range(60,70):
    temp_flavor_text = random.choice(just_right_flavor)
    temp_desc = "Looks like its just right outside with"
elif temp_farenheit in range(50,60):
    temp_flavor_text = random.choice(cold_flavor)
    temp_desc = "Looks like it might be pretty cold with"
elif temp_farenheit < 50:
    temp_flavor_text = random.choice(freezing_flavor)
    temp_desc = "Looks like its going to be freezing with"


wakeup_text_list = ["Get cho money up not cho funny up. Wake the fuck up",
 "Remember as drake once said. Almost drowned in her pussy so I swam to her butt", 
 "Good morning! Justin Timberlake once said, what you gonna do with all that meat",
 "Patrick Bateman once said. I like to disect girls. Did you know im utterly insane?",
 "I feel lethal, on the verge of frenzy. I think my mask of sanity is about to slip. - Patrick Bateman",
 "Dont forget to return those video tapes today.",
 "As your fellow sigma male, Patrick Bateman, once said. You're a fucking ugly bitch. I wanna stab you to death, and play around with your blood.",
 "Chow says, you gonna fuck on me? Alan says, nobodies gonna fuck on you, i'm on your side, I hate godzilla, I hate him too, I hate him, He destroys cities, please, this isn't your fault, ill get you some pants.",
 "As phil once said. Paging doctor faggot.",
 "As dave harkin once said. Life is a marathon, and you cant win a marathon without putting a few bandaids on your nipples.",
 "As Kurt Buckman once said. I'd like to bend her over a barrel and show her the fifty states",
 "So you took the penis foods as an invitation to fuck her? - Dale Arbus",
 "Technically I think it's immoral not to kill him - Kurt Buckman",
 "Muhammad is the most commonly used name on Earth. Read a fucking book for once!",
 "Prepare to be fucked by the long dick of the law.",
 "I hate to break it to you but the american dream is made in china",
 "Infultrate the dealer, find the supplier. -Ice Cube",
 "principal dadier once said. I'm one black gay kid getting puched in the face away from a nervous breakdown",
 "Sir, if I have to suck someone's dick... I will but I prefer not to.",
 "Oh, Fuzz Aldrin. How many times have I told you to use the litter box?",
 "They probably can't even track those things",
 "It's almost a shame to smoke it. It's like killing a unicorn with a bomb",
 "War is upon you, prepare to suck the cock of karma",
 "You assholes do what I say or i'm gonna take you outside and fuck you in the street",
 "They hate a us because they ain't us",
 "Im not gonna call him father, even if there's a fire"
]

if skys == "snow":
    weather_status = "Holy fucking shit. Its fucking snowing outside. What the fuck are you still doing inside."
elif "cloud" in skys:
    weather_status = f"You might get a little shade today with {skys} in the skies"
elif "rain" in skys:
    weather_status = f"Make sure you bring an umbrella today because there is some {skys} today"
elif "storm" in skys:
    weather_status = "Make sure you put the kites up today, because theres a nice thunderstorm at the moment"
elif "clear" in skys:
    weather_status = "Make sure to wear your sunglasses this morning because the sun is currently out!"
else:
    weather_status = f"The weather status today is {skys}"



video = input("Paste the video you want to play when you wake up: ")

alarm = input("What time would you like to wake up: ")

while True:


    t = time.localtime()
    current_time = time.strftime("%H:%M", t)

    # Delete when done!!!!
    # current_time = '10'

    if current_time == f'{alarm}':

        wakeup_text = random.choice(wakeup_text_list)
        
        tts = gtts.gTTS(f"""
            {wakeup_text}. {temp_desc} {city} at a {temp_flavor_text} {temp_farenheit} degrees today, but its supposed to feel about {feels_like_farenheit} degrees. {weather_status}.

         """)



        # save the audio file
        tts.save("hello.mp3")

        # play the audio file
        playsound("wakeup.wav")
        playsound("hello.mp3")

        webbrowser.open(f'{video}')

        time.sleep(10)

        pyautogui.press("f")


        break
    else:
        pass



if os.path.exists("hello.mp3"):
    os.remove("hello.mp3")
else:
    print("The file does not exist")