def main():
    # Prompt user for time and pass input into the convert function: store value in time
    time = convert(input("What time is it? ").strip())
    """breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00 (12:00 p.m. and 1:00 p.m.), and dinner between 18:00 and 19:00 (6:00 p.m. and 7:00 p.m.)"""
    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")

# A function that converts time to the corresponding number of hours as a float
def convert(time):
    hours, minutes = map(int, time.replace(
        "a.m.", "").replace("p.m.", "").split(":"))
    if "p.m." in time and hours != 12:
        hours += 12
    if "a.m." in time and hours == 12:
        hours = 0
    return hours + minutes / 60


if __name__ == "__main__":
    main()
