#Indoor CS50
def main():
     name = input("Enter your name: ").lower().strip()
     print(f"My name is {name}")
main()


#PlayBackSpeed CS50
name = input("Type Here: ")
name = name.replace(" ", "...")
print(name)


#MakeFaces CS50
text = input("Enter text: ")
#replace 
text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")

print(text)

#Einstein

m = int(input("Enter mass: "))
c = 300000000 

E = m * c ** 2
print(E)

#tip calulator

dollar = float(input("How much was your meal: "))     
percent = float(input("What percent of the meal you want to tip: "))
tip = dollar * (percent / 100)

print(f"The tip of the meal is ${tip}")