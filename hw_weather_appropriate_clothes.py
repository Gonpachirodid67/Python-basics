temparature = float(input("What is today's temparature?:"))

if isinstance(temparature, (int, float)) and not isinstance(temparature, bool):
    if temparature > -99999999999999999999999999999 and temparature <=-15:
        print("That's a nice joke cause you wouldn't be able to live in such temparature because you might freeze.")
    elif temparature > -15 and temparature <=0:
        print("You should wear a thick winter coat, sweater, gloves, scarf, and warm shoes.")
    elif temparature > 10 and temparature <=20:
        print("You should wear a light jacket, sweater, long pants, and closed shoes.")
    elif temparature > 20 and temparature <=30:
        print("You should wear a t-shirt and jeans or light pants should be fine.")
    elif temparature > 30 and temparature <=35:
        print("You should wear light, loose clothes like a t-shirt and shorts.")
    elif temparature > 35 and temparature <=45:
        print("You should wear very light, breathable clothes and drink plenty of water and stay in the shade.")
    elif temparature > 45 and temparature <=50:
        print("You should avoid going out and wear very light clothes in a air-cooled room.")
    elif temparature > 50 and temparature <=999999999999999999999999999999999999999999999:
        print("That's a nice joke cause the max temparature you could live in is 50*C.")
else:
    print("Please input a number.")