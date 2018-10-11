Celsius = eval(input("De tempratuur in Celsius: "))


def convert(Celsius):
    Fahrenheit = Celsius * 1.8 +32
    print("De tempratuur is " + str(Celsius) + " in Celsius. Dit is " + str(Fahrenheit) + " in Fahrenheit.")
    return Celsius

def table(Celsius):
    convert(Celsius)

    print()

    print("  F        C")
    for i in range(Celsius, 50, 10):
        print("{:1.1f} {:8.1f}".format(i * 1.8 + 32, i))


table(Celsius)
