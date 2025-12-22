print("=" * 40)
print("        🔐 USERNAME GENERATOR")                    # Title of the Project
print("=" * 40)


print("\nWelcome! Let's create some username ideas for you 😊\n")

first=input("Input your First Name :").strip().lower()
last=input("Input your Last Name :").strip().lower()
number=input("Input your Birth Year or Lucky Number :").strip()

u1= first + last
u2=first + "_" + last
u3 = first[0] + last + number
u4 = last + first
u5=first[0]+last[0]+number

print("\n" + "-" * 40)
print("✨ Username Suggestions")
print("-" * 40)

print ("01. "+u1)
print ("02. "+u2)
print ("03. "+u3)
print ("04. "+u4)
print ("05. "+u5)

print("-" * 40)