import instaloader
import pyperclip

profile=input("Enter Username Instagram: ")
L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, profile)
pyperclip.copy(profile.profile_pic_url)

print("Username:", profile.username)
print("Full Name:", profile.full_name)
print("Profile Pic URL:", profile.profile_pic_url)
print("Finish Copy URL!!")