# Done by Carlos Amaral (2020/09/13)


from tkinter import *
import random
import string


window = Tk()
window.wm_title("Password generator")
window.geometry("258x220")


# Function to generate passwords
def generate_password():
    characters = 'abcdefghijklmnopqrstuvixyz0123456789ABCDEFGHIJLMNOPQRSTUVXYZK!?*$€'
    password = ''

    # loop to generate password with the length provided by user
    for x in range(char_num.get()):
        password += random.choice(characters)

        #or
       #password = password + random.choice(characters)

    gen_pass.set(password)



# Presentation label
pres_label = Label(window, text="Password generator", font=('bold',19))
pres_label.grid(row=0, column=0)

# Blank label
Blank_label = Label(window, text="")
Blank_label.grid(row=1, column=0)


# Character_number label
char_label = Label(window, text="Number of characters")
char_label.grid(row=2, column=0)


# Blank label
Blank_label = Label(window, text="")
Blank_label.grid(row=4, column=0)

# Password label
pass_label = Label(window, text="Password")
pass_label.grid(row=5, column=0)




# Text box for character_number
char_num = IntVar()
entry_num = Entry(window, textvariable=char_num)
entry_num.grid(row=3, column=0)


# Text box for generated password
gen_pass = StringVar()
generated_pass = Entry(window, textvariable=gen_pass)
generated_pass.grid(row=6, column=0)


# Generate password button
button_generate = Button(window, text="Generate", command=generate_password)
button_generate.grid(row=7, column=0)


window.mainloop()
