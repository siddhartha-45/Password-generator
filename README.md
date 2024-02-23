# Password-generator
This Python script generates a random password based on the user's input for the length of the password. 
Here's how it works:
It imports the string and random modules.
It creates a string gen_password containing all ASCII letters, digits, and punctuation characters. This string will be used to generate the random password.
It prompts the user to enter the desired length of the password.
It uses random.choices() to select characters randomly from gen_password with replacement, k times (where k is the length of the password).
It joins these random characters together to form the password.
It prints the generated password.
