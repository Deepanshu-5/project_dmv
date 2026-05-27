print("this is a weather recommendation system")
temp=float(input("enter the temperature in degree celsius"))
if temp>35:
    print("it is hot outside, wear light clothes and stay hydrated")
elif temp>20:
    print("it is good outside, go out and enjoy the weather")
elif temp>10:
    print("it is cool outside, wear a jacket")
else:
    print("it is cold outside, wear warm clothes")