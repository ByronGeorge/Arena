#Where all the spells for the classes will be
#for 'passive' should be yes or no and it will not have a cd or just unique to class
#for 'effect' this will be things like, daze, slow, bleed, sap
#for 'successRate' this will be hitchance
#for 'AoE' should be yes or no



class spells:
    def gladiator(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range, level):
        """Gladiator spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Gladiators should be strong melee characters with strength to take down their foes."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range
        self.level = level



    def archer(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range, level):
        """Archer spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Archers should be agile ranged damage that use traps and different arrow techniques to take down their foes."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range
        self.level = level


    def mage(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range, level):
        """Mage spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Mages should be strong ranged casters that can do high burst magic damage."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range
        self.level = level
    
    def priest(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range):
        """Priest spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Priests should be a necessity in a party by providing support such as heals, remedies, and aid to any battle. While they have strong support abilities, they have DoTs too."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range

    def mischief(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range, level):
        """Mischief spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Mischiefs should be agile melee characters that use a dualwield technique to elimate their foes. They know all the tricks of the trade."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range
        self.level = level

    def jester(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range, level):
        """Jester spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Jesters use tricks to decieve their foes."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range
        self.level = level

    def titan(self, description, passive, magicDamage, physicalDamage, effect, cooldown, manaCost, healthCost, staminaCost, successRate, AoE, range, level):
        """Titan spell inputs: 'description', 'passive', 'magicDamage', 'physicalDamage', 'effect', 'cooldown', 'manaCost', 'healthCost', 'staminaCost', 'successRate', 'AoE', 'range'.
        Titans should be strong melee tanks that are on the front line of battle."""
        self.description = description
        self.passive = passive
        self.magicDamage = magicDamage
        self.physicalDamage = physicalDamage
        self.effect = effect
        self.cooldown = cooldown
        self.manaCost = manaCost
        self.healthCost = healthCost
        self.staminaCost = staminaCost
        self.successRate = successRate
        self.AoE = AoE
        self.range = range
        self.level = level
