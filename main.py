import requests
from config import APP_ID, APP_KEY, NUTRITIONX_URL
import datetime as dt

nlp_url = f"{NUTRITIONX_URL}/v2/natural/exercise"
query = input("What exercise did you did today\n")
body = {
    "query": query
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
nlp_resp = requests.post(url=nlp_url, json=body, headers=headers)
nlp_resp.raise_for_status()
exercise_data = nlp_resp.json()['exercises']

date = dt.datetime.now().today().date()
time = dt.datetime.now().time()
print("Date:", date, "Time:", time)
formatted_date = date.strftime("%d/%m/%Y")
formatted_time = time.strftime("%I:%M:%S %p")


for exercise in exercise_data:
    body = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "duration": exercise['duration_min'],
            "exercise": exercise['user_input'],
            "calories": exercise['nf_calories']
        }
    }
    sheety_headers = {
        "Authorization": "Bearer dklajfadksjfsfksdaio"
    }
    sheety_url = "https://api.sheety.co/582c8f947665832aaca2ae9c6e8b3ce4/myWorkouts/workouts"
    resp = requests.post(sheety_url, json=body, headers=sheety_headers)
    print(resp.text)
