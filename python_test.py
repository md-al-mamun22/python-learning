Name = ("mamun")
age = (18)

print(Name)
print(age)

Services =['acupuncture', 'yoga', 'massage']

for service in Services:
    print(service)



    def add_numbers(num1, num2):
        result = num1 + num2
        return result
    output = add_numbers (5,7)
    print(output)




client_info = {
    "name" : "Md Al Mamun",
    "Problem" : "software login error",
    "Urgency" : "High"
}


if client_info ["Urgency"].lower() == "High":
    print ("জরুরি appointment দরকার")
else:
    print ("সাধারণ appointment।")