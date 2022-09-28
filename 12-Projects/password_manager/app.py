from datetime import datetime
from getpass import getpass

def add():
   name = input("Account name: ")
   password = getpass("Password: ")
   with open("passwords.txt", "a") as f:
      f.write(f"{name}|{password}\n")


def view():
   with open("passwords.txt", "r") as f:
      for line in f.readlines():
         data = line.rstrip()
         name, password = data.split("|")
         print(f"Name: {name} - Password: {password}")


def export():
   with open("passwords.txt", "r") as f:
      for line in f.readlines():
         name, password = line.split("|")
         t = datetime.now()
         file_name = f"export-{t.year}-{t.month}-{t.day}-{t.hour}-{t.minute}-{t.second}.csv"
         with open(file_name, "a") as f:
            f.write(f"{name},{password}")


key = getpass("Please enter master key: ")

if key == "1234":
   while True:
      mode = input("Would you like to add a new password or view existing ones or export all (view, add, export), press q to quit? ").lower()

      if mode == 'q':
         break

      elif mode == 'add':
         add()
      elif mode == 'view':
         view()
      elif mode == 'export':
         export()

      else:
         print("Invalid mode")
         continue

else:
   print("Your key incorrect")
