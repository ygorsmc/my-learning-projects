#Greeting the user
print("Hello my dear. It's time to creat you band name!")
#Ask for the job that they like the most
like_job = input("What's the job you appreciate the most?\n")
print(f"{like_job}... Let's to the next step.")
#Ask for a pet name of the user
pet_name = input("What's the name of your favorite pet? If you don't have one then give the first name that comes to your mind...\n")
print(f"{pet_name} it's a really a good name!)
print("Then let's combine these two names.")
#Combine the given names
band_name = f"{like_job} {pet_name}"
print(f"The creation result is {band_name}!")
