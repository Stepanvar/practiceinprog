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

class	Property(Info):
	"""sell, buy, get_damage, del
	"""
	def	__init__(self):
		self.size = 10
	# def	__del__(self):
	# 	print("your building destructed")
	def _sell(self):
		pass
	def _buy(self):
		pass
	def	_get_damage(self, damage):
		"""count damage to certain property

		Args:
			damage (int): damage to property

		Returns:
			int: health of building
			int: remain damage
		"""
		self.health = self.health - damage
		if (self.health < 0):
			damage -= self.health 
			self.health += damage
			print ("property tottaly destroyed")
			print ("health: %d, remain damage: %d\n" %(self.health, damage))
			return self.health, damage
		elif (self.health == 0):
			print ("property destroyed")
			print ("health: 0, remain damage: 0\n")
			return 0, 0
		else:
			print ("property alive with health: %d\n" %self.health)
			return self.health, 0


class	UsersField(Info):
	def	__init__(self):
		self.activated_cards = []
	def	_activate_card(self, instance):
		self.activated_cards.append(instance)

class	Mine(Property, Info):
	def	__init__(self):
		self.health = 10
		self.production = random.randint(1, 5)
		self.cost = self.production * 2
	def	__str__(self):
		return "mine"

class	Wall(Property, Info):
	def	__init__(self):
		self.cost = random.randint(1, 6)
		self.health = self.cost * 2
	def	__str__(self):
		return "wall"

class	Creep(Property, Info):
	def	__init__(self):
		self.attack = random.randint(1, 3)
		self.health = random.randint(1, 3)
		self.cost = round((self.attack + self.health) / 2)
	def	attack(self, instance):
		instance._get_damage(attack)
	def	__str__(self):
		return "creep"

class	Spell(Property, Info):
	def	__init__(self):
		self.attack = random.randint(4, 10)
		self.cost = self.attack
		self.health = self.attack
	def	attack(self, instance):
		instance._get_damage(attack)
	def	__str__(self):
		return "spell"

class	User(Property, Info):
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
		self.nmb = 1
		for card in self.user_hand:
			print("%d." %self.nmb, end='')
			self._print_name(card)
			self._print_attr(card)
			self.nmb += 1
	def	__str__(self):
		return "user"

class	Talon(Info):
	def	__init__(self, all_cards):
		self.mines_count = round(all_cards / 4)
		self.spells_count = round(all_cards / 4)
		self.walls_count = round(all_cards / 4)
		self.creeps_count = round(all_cards / 4)
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
end = 1
while (end):
	user1._cards_in_hand()
	i_hand = int(input("Enter index of card to activate\n")) - 1
	if (user1.balance > 0 and user1.balance - user1.user_hand[i_hand].cost > 0 and i_hand in range(len(user1.user_hand))):
		user1.user_hand.pop(i_hand)
		user1.user_activated_cards._activate_card(user1.user_hand[i_hand])
		user1.balance -= user1.user_hand[i_hand].cost
		print("activated cards")
		for i_active in range(len(user1.user_activated_cards.activated_cards)):
			user1._print_name(user1.user_activated_cards.activated_cards[i_active])
			user1._print_attr(user1.user_activated_cards.activated_cards[i_active])
			if (type(user1.user_activated_cards.activated_cards[i_active]).__name__ == Spell.__name__):
				i_attack = int(input("Choose property to attack\n")) - 1
				user1.user_activated_cards.activated_cards[i_attack]._get_damage(user1.user_activated_cards.activated_cards[i_active].attack)
				user1.user_activated_cards.activated_cards.pop(i_active)
	else:
		print("you can't afford it")	
	end = int(input("Do you want to continue your move? 1 - yes, 0 - no\n"))