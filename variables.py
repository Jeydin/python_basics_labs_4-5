name = input("What is your name? ")
age = input("How old are you? ")
lastbirthday = input("What year was your last birthday? ")

birthyear = int(lastbirthday) - int(age)
print("Your name is " + name + " and you are " + age +
      " years old\nYou were born in " + str(birthyear))
