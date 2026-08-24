#This is main.py

import tkinter as tk
import requests
from AQI_Tracker_Ver1.hazards import get_hazard_color
from AQI_Tracker_Ver1.aqi_fetcher import AQI_data, update_user_aqi, locational_data

def get_AQI():
    zipcode = zip_entry.get()
    update_user_aqi(zipcode)
    results_box.delete("1.0", tk.END)

    report = AQI_data(zipcode)
    aqi_value = locational_data["UserLocation"]["AQI"]
    color = get_hazard_color(aqi_value)

    results_box.insert(tk.END, report)

    # Apply color to the whole report
    results_box.tag_add("aqi_color", "1.0", tk.END)
    results_box.tag_config("aqi_color", foreground=color)
    results_box.see(tk.END)

def show_json():
    results_box.delete("1.0", tk.END)

    for city in locational_data.keys():
        url = locational_data[city]["url"]


        import json
        response = requests.get(url).json()

        results_box.tag_config("json_color", foreground="white")
        results_box.insert(tk.END, f"\n--- {city} JSON ---\n")
        results_box.insert(tk.END, json.dumps(response, indent=4), "json_color")
        results_box.insert(tk.END, "\n\n")


window = tk.Tk()
window.title("My AQI TRACKER")
zip_entry = tk.Entry(window)
zip_entry.bind("<Return>", lambda event: get_AQI())
zip_entry.pack()

# TODO: Add new function and change AQI REPORT to a compare zipcodes function.
button1 = tk.Button(window, text="AQI REPORT", command=get_AQI)
button1.pack()
button2 = tk.Button(window, text="API → JSON", command=show_json)
button2.pack()

results_box = tk.Text(window, width=150, height=50, font=("Arial", 12))
results_box.config(bg="black")
results_box.pack()
window.mainloop()
