def main():
    # Prompt user for time
    time = input("What time is it? ")
    # Call the convert function, and store return value in x
    x = convert(time)
    """breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00"""
    if 7.00 <= x <= 8.00:
        print("It is breakfast time")
    elif 12.00 <= x <= 13.00:
        print("It is lunch time")
    elif 18.00 <= x <= 19.00:
        print("It is dinner time")
    else:
        pass

# A function that converts time to the corresponding number of hours as a float
def convert(time):
    hours, minutes = (time.split(":"))
    converted_hours = float(hours)
    converted_mins = float(minutes)
    return converted_hours + (converted_mins / 60)


if __name__ == "__main__":
    main()
