import random
import pygame as pg
class	Info:
	"""print information about name and attribures of instance
	"""
	def	_print_name(self, instance):
		print(instance)
	def	_print_attr(self, instance):
		for attr in dir(instance):
			if not attr.startswith('_'):
				print(attr, end=':')
				print(getattr(instance, attr), end=' ')
		print("\n")

class	Operations(Info):
	"""control operations on object
	"""
	pass

class	UsersField(Info):
	def	__init__(self):
		self.activated_cards = []
	def	_activate_card(self, instance):
		self.activated_cards.append(instance)

class	Mine(Operations, Info):
	def	__init__(self):
		self.health = 10
		self.production = random.randint(1, 5)
		self.cost = self.production * 2
	def	__str__(self):
		return "mine"

class	Wall(Operations, Info):
	def	__init__(self):
		self.cost = random.randint(1, 6)
		self.health = self.cost * 2
	def	__str__(self):
		return "wall"

class	Creep(Operations, Info):
	def	__init__(self):
		self.damage = random.randint(1, 3)
		self.health = random.randint(1, 3)
		self.cost = round((self.damage + self.health) / 2)
	def	__str__(self):
		return "creep"

class	Spell(Operations, Info):
	def	__init__(self):
		self.damage = random.randint(4, 10)
		self.cost = self.damage
		self.health = self.damage
	def	__str__(self):
		return "spell"

class	User(Operations, Info):
	"""interactions with user"""
	def	__init__(self):
		self.health = 50
		self.balance = 50
		self.user_hand = []
		self.user_activated_cards = UsersField()
	def	_get_card(self, i):
		"""get card from talon

		Args:
			i (int): number of card needed

		Returns:
			void: append card to the user_hand
		"""
		while (i > 0):
			obj = talon1._give_card()
			self.user_hand.append(obj)
			i -= 1
	def	_cards_in_hand(self):
		for card in self.user_hand:
			self._print_name(card)
			self._print_attr(card)
	def	__str__(self):
		return "user"

class	Talon(Info):
	def	__init__(self, all_cards):
		self.mines_count = round(all_cards / 4)
		self.spells_count = round(all_cards / 4)
		self.walls_count = round(all_cards / 4)
		self.creeps_count = all_cards - self.mines_count - self.spells_count - self.walls_count
	def	_give_card(self):
		"""Choose random class and make it instance

		Returns:
			instance: instance of random class
		"""
		list = [Mine(), Spell(), Wall(), Creep()]
		obj = random.choice(list)
		if (type(obj).__name__ == Mine.__name__):
			self.mines_count -= 1
		elif (type(obj).__name__ == Spell.__name__):
			self.spells_count -= 1
		elif (type(obj).__name__ == Wall.__name__):
			self.walls_count -= 1
		elif (type(obj).__name__ == Creep.__name__):
			self.creeps_count -= 1
		else:
			print ("error in give_card")
		if (self.mines_count == 0 or self.spells_count == 0 or self.walls_count == 0 or self.creeps_count == 0):
			print("talon end")
			exit()
		return obj

	def	__str__(self):
		return "talon"


nmb_cards = int(input("enter amount of cards in game\n"))
talon1 = Talon(nmb_cards)
user1 = User()
user1._get_card(5)
user1._cards_in_hand()
i = int(input("enter index of your card\n"))
print(user1.user_hand[i])
user1.user_activated_cards._activate_card(user1.user_hand[i])
user1._print_attr(user1.user_activated_cards.activated_cards[0])
