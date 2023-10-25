def main():
    user_input = input("What time is it? ")
    convert(user_input)


def convert(time):
    time = time.strip().split(":")
    for i in range (len(time)):
        time[i] = int(time[i])
    time[1] = time[1] / 60
    time = time[0] + time[1]
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("")
    return time



if __name__ == "__main__":
    main()