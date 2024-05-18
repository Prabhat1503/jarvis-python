import speech_recognition as sr

# Function to get location through speech
def get_location():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say the location for weather information:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        location = recognizer.recognize_google(audio)
        print("You said:", location)
        return location
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None

# Get location through speech
location = get_location()

# Construct the search query and URL
if location:
    search = f"weather in {location}"
    url = f"https://www.google.com/search?q={search}"
    print("Search URL:", url)
else:
    print("No location provided.")
