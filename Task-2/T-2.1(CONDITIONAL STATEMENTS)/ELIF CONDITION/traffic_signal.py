print("this is traffic signal simulator")
color=input("enter the color of traffic signal").lower().strip()
if color=="red":
    print("stop")
elif color=="yellow":
    print("ready")
elif color=="green":
    print("go")
else:
    print("invalid color")