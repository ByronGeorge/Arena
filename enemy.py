from msilib import type_key


class Enemy:

    def __init__(self, health, mana, armor, magicResistance, magicDamage, physicalDamage,enemyType,enemyName,dexterity):
        self.health = health
        self.mana = mana
        self.armor = armor
        self.magicResistance = magicResistance
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.enemyType = enemyType
        self.enemyName = enemyName
        self.dexterity = dexterity
