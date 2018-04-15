"""Password geenrator program wrriten in python 
   By: Fon Desmond Ade
   Email: adedesmond6@gmail.com"""


import random

class PasswordGenerator:
	'''Generates password mix with capital letters, 
	   special characters and lower letters'''

	def __init__(self):

		self.number = list(range(10))#generates a list of numbers 0-9
		self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
		self.special_characters = '@=+$^&*()|?><<?|/[]{\}'
		self.capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


	def generate_weak_password(self):
		'''Selects a random letters to and adds it to password'''
		password = ''
		for n in range(4):
			password += random.choice(self.letters)
			password += random.choice(self.letters)
			

		return password


	def generate_strong_password(self):

		'''Selects  random letters mix with Caps,
		   lower, and special characters  and increments
		   password with it so as to generate password'''

		password = ''
		for i in range(6):
			password += random.choice(self.letters)
			password += str(random.choice(self.number))
			password += random.choice(self.special_characters)
			password += random.choice(self.capital_letters)

		#print('This is your password')
		return password

class Menu:
	def __init__(self):
		self.password_generator = PasswordGenerator() 


	def display(self):
		'''Displays the menu'''
		print('''

			Welcome to password generator
			----------------------------
			Choices--

			Enter 2 for weak password
			Enter 3 for strong password

			''')

	def run(self):
		while True:
			self.display()
			try:
				choice = int(input('Enter your choice'))

				if choice == 2:
					print(self.password_generator.generate_weak_password())
				elif choice == 3:
					print(self.password_generator.generate_strong_password())

				else:
					print('Invalid choice')
			except ValueError as e:
				print('Make sure to enter a choice')


if __name__ == '__main__':
	Menu().run()


