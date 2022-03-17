
#I think classes should just be stat boosters with scaling, instead of flat health, mana , damage. 
#We can just raise these stats during level ups which still makes characters unique
#'stamina' could be used as energy

class classes:

    def gladiator(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Gladiator, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.)
        Gladiators should excel in strength > vigor > dexterity > stamina."""
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit

    def archer(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Archer, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.
        Archers should excel in dexterity > strength > intelligence > vigor."""
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit

    def mage(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Mage, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.
        Mages should excel in intelligence > spirit > dexterity > vigor."""
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit
    
    def priest(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Priest, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.
        Priests should excel in spirit > intelligence > vigor > dexterity."""
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit

    def mischief(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Mischief, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.
        Mischiefs should excel in dexterity, strength > stamina > vigor."""
        #This is the rogue 
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit

    def jester(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Jester, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.
        Jesters should excel in luck > dexterity > intelligence = strength."""
        #Jesters will have the most luck as a base stat.
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit

    def titan(self, armor, magicResistance, dexterity, strength, intelligence, stamina, luck, vigor, spirit):
        """Class Titan, assign stats: 'armor', 'magicResistance', 'dexterity', 'strength', 'intelligence', 'stamina', 'luck', 'vigor', 'spirit'.
        Titans should excel in vigor, armor, stamina, dexterity."""
        #would use stamina
        #These are the tanks
        self.armor = armor
        self.magicResistance = magicResistance
        self.dexterity = dexterity
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.luck = luck
        self.vigor = vigor
        self.spirit = spirit
