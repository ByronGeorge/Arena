class Player:
    def __init__(self, health, mana, armor, magicResistance, magicDamage, physicalDamage, playerType, playerName, dexterity, playerClass, luck, stamina, language, level, strength, intelligence):
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