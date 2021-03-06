class Player:
    def __init__(self, health, mana, armor, magicResistance, magicDamage, physicalDamage, playerType, playerName, dexterity, playerClass, luck, stamina, language, level, strength, intelligence, vigor, spirit):
        self.health = health
        self.mana = mana
        self.armor = armor
        self.magicResistance = magicResistance
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.playerType = playerType
        self.playerName = playerName
        self.dexterity = dexterity
        self.playerClass = playerClass
        self.luck = luck
        self.stamina = stamina
        self.language = language
        #was thinking we could maybe have multiple languages and you need people who can speak each one to reveal secrets. 
        #We can also implement an item with this that decrypts/translates messages 
        self.level = level
        self.strength = strength
        self.intelligence = intelligence
        self.vigor = vigor
        self.spirit = spirit

        # Good job Christopher! I also like that you added levels to both the player class and enemy class. Good thinking. I also like the idea of the languages - BG
        # we can make little puzzles based off the languages they know - BG
