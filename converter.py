def convert_celsius():
    while True:
        get_celsius=input("Enter the temperature in celsius: ")
        try:
            celsius=float(get_celsius)
            farenheit=(celsius*1.8)+32
            return farenheit
        except ValueError:
            print("Invalid Option,Please enter valid temperature")
            continue
def convert_weight():
    while True:
        get_weight=input("Enter the weight in Kilograms: ")
        try:
            weight=float(get_weight)
            pound=weight*2.2
            return pound
        except ValueError:
            print("Invalid Option, Please enter valid weight")
            continue
while True:
    print("Menu \n1.Celsius to Farenheit \n2.Kilogram to Pound \n3.Exit")
    userinput=input("Select the Option from the Menu: ")
    if userinput=="1":
        temp=convert_celsius()
        print("The temperature in Farenheit is: ",temp)
    elif userinput=="2":
        weight=convert_weight()
        print(f"The weight in Pounds is: {weight:.2f}")
    elif userinput=="3":
        print("Thankyou")
        break
    else:
        print("Invalid option, Please enter the correct option")
        continue
