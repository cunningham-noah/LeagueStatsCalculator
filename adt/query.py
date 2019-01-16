from stats_adt import *


class Query(object):
    """Class to perform queries on a champion."""

    def __init__(self, level: 'int', champion: 'str'=''):
        self.level = level
        self.multiplier = level - 1
        self.champion = champion

    def __str__(self):
        return "<Query({}) object at {}>".format(self.champion, hex(id(self)))

    def __repr__(self):
        return "Query({})".format(self.champion)

    def multiply_helper(self, attrs):
        stats_dict = dict()
        for x in range(len(attrs)):
            if attrs[x][1][:2] == 'hp':
                if attrs[x][1][2] == 'R':
                    stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['hpRegen']})
                else:
                    stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['hp']})
            elif attrs[x][1][:2] == 'mp':
                if attrs[x][1][2] == 'R':
                    stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['mpRegen']})
                else:
                    stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['mp']})
            elif attrs[x][1][:2] == 'mr':
                stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['mr']})
            elif attrs[x][1][:2] == 'ar':
                stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['armor']})
            elif attrs[x][1][:2] == 'at':
                if attrs[x][1][6] == 'S':
                    stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['attackSpeed']})
                else:
                    stats_dict.update({attrs[x][0]: (champions[self.champion][attrs[x][1]]*self.multiplier)+champions[self.champion]['attackDamage']})
        return stats_dict

    def multiply(self):
        attributes = (
            ('hp', 'hpPerLevel'),
            ('hpRegen', 'hpRegenPerLevel'),
            ('mp', 'mpPerLevel'),
            ('mpRegen', 'mpRegenPerLevel'),
            ('mr', 'mrPerLevel'),
            ('armor', 'armorPerLevel'),
            ('attackSpeed', 'attackSpeedPerLevel'),
            ('attackDamage', 'attackDamagePerLevel'),
        )
        return self.multiply_helper(attributes)

    def readout(self):
        obj = self.multiply()
        for key, value in obj.items():
            print("{<25}: {}".format(key, value))


def createChampionQuery():
    champion = input("Champion name: ").lower()
    while not champions[champion]:
        champion = input("Champion name: ").lower()

    level = int(input("Champion level: "))
    while not level <= 1 and not level <= 18:
        level = int(input("Champion level: "))

    championObject = Query(level, champion)
    return championObject


def lowercase_all_dict_items(dictionary):
	"""Convert all keys, values, and keys of values to lowercattackSpeede in the
	champions dictionary for user input validation. O(n*m) time O(1) space.
	"""
	dictionary = {key.lower(): value for key, value in dictionary.items()}
