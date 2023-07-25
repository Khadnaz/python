import os

if os.path.exists(r"C:\Users\User\Documents\Learnings\Python_scripts\demofile.txt"):

 os.remove(r"C:\Users\User\Documents\Learnings\Python_scripts\demofile.txt")

else:
  print("The file does not exist")