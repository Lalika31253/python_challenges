name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
fav_namber = int(input("Enter tour favorete number: "))

cm_height = height * 100

print(f"=====================================")
print(f"YOUR PROFILE CARD")
print(f"=====================================")

print(f"Name               {name}")
print(f"Age                {age}")
print(f"Height             {height:.2f} m ({cm_height:.0f} cm)")
print(f"Favorite Number    {fav_namber}")

print(f"====================================")