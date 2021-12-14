merchantItemPrices = {
    'HEALTH_POTION': 15,
    'ATTACK_POTION': 20,
    'WOOD_SHIELD': 100,
    'IRON_SHIELD': 150,
    'DRAGON_SHIELD': 300,
    'WOOD_SWORD': 150,
    'IRON_SWORD': 200,
    'DRAGON_SLAYER': 400,
}

class GameCharacter:
  maxHealth = 100
  maxMana = 100
  basicDamage = 15
  maxItemNumber = 4

  ability_types = {
    'damage': 'DAMAGE',
    'healing': 'HEALING',
    'damage_increase': 'DAMAGE_INCREASE',
    'mana_regen': 'MANA_REGENERATION',
    'resurrection': 'RESURRECTION'
}

  abilities = {
    'Aegis Assault': {
        'value': 16,
        'cost': 10,
        'type': ability_types['damage']
    },
    'Alpha Strike': {
        'value': 20,
        'cost': 12,
        'type': ability_types['damage']
    },
    'Audacious Charge':{
        'value': 15,
        'cost': 8,
        'type': ability_types['damage']
    },
    'Arcane Barrage':{
        'value': 99,
        'cost': 80,
        'type': ability_types['damage']
    },
    'Blade of the Ruined King': {
        'value': 28,
        'cost': 12,
        'type': ability_types['damage']
    },
    'Bullet Time': {
        'value': 50,
        'cost': 39,
        'type': ability_types['damage']
    },
    'Celestial Blessing': {
        'value': 100,
        'cost': 30,
        'type': ability_types['healing']
    },
    'World Ender': {
        'value': 100,
        'cost': 100,        
        'type': ability_types['damage']
    },
    'Divine Ascent': {
        'value': 100,
        'cost': 0,
        'type': ability_types['mana_regen']
    },
    'Star Call': {
        'cost': 100,
        'type': ability_types['resurrection']
    }
}

  def __init__(self):
    self.currentHealth = GameCharacter.maxHealth
    self.currentDamage = GameCharacter.basicDamage
    self.currentMana = GameCharacter.maxMana
    self.inventory = []
    self.gold = 1000
  
  def basicAttack(self, target):
    target.takeDamage(self.currentDamage)

  def takeDamage(self, damage):
    self.currentHealth -= damage

  def buyItem(self, itemName):
    hasItem = itemName in merchantItemPrices.keys()
    if hasItem != True:
      return print("Item name is not found")

    itemPrice = merchantItemPrices[itemName]
    if itemPrice <= self.gold:
      if len(self.inventory) < GameCharacter.maxItemNumber:
        self.inventory.append(itemName)
        self.gold -= merchantItemPrices[itemName]
      else:
        return print("You have a full inventory and you cannot buy anything else")
    else:
      return print("Insufficient gold")
  
  def sellItem(self, itemName):
    hasItem = itemName in merchantItemPrices.keys()
    if hasItem != True:
      return print("Item name is not found")

    if itemName in self.inventory:
      self.inventory.remove(itemName)                          
      self.gold += merchantItemPrices[itemName] * 0.8
    else:
      return print("You do not have this item")

  def castAbility(self, abilityName, target):
    isAbilityInDictionary = abilityName in GameCharacter.abilities.keys()
    if isAbilityInDictionary == True:
      ability = GameCharacter.abilities[abilityName]

      if self.currentMana >= ability['cost']:
        self.currentMana = self.currentMana - ability['cost']

        if ability['type'] == GameCharacter.ability_types['damage']:
          if target.currentHealth > 0:
            target.takeDamage(ability['value'])
          else:
            print("Target is already dead")
        
        if ability['type'] == GameCharacter.ability_types['healing']:
          if target.currentHealth > 0:
            if target.currentHealth + ability['value'] <= target.maxHealth:
              target.currentHealth += ability['value']
            else:
              target.currentHealth = target.maxHealth
          else:
            print("Target is already dead, cannot heal a dead character!")
        
        if ability['type'] == GameCharacter.ability_types['mana_regen']:
          if target.currentMana + ability['value'] <= target.maxMana:
            target.currentMana += ability['value']
          else:
            target.currentMana = target.maxMana

        if ability["type"] == GameCharacter.ability_types['resurrection']:
          if target.currentHealth <= 0:
            target.currentHealth = GameCharacter.maxHealth
            target.currentMana = GameCharacter.maxMana
          else: 
            return print("Invalid Move : Target is still standing")

      else:
        return print("Mana is not enough to cast this ability")   
    else:
      return print("This ability does not exist!")

  @classmethod
  def percentageHealthRemaining(cls, health):
    return str(round(health / cls.maxHealth * 100)) + '%'

character1 = GameCharacter()
character2 = GameCharacter()

print(character1.currentMana)
print(character2.currentHealth)

character1.castAbility('Bullet Time', character2)
print(character2.currentHealth) 
character1.castAbility('Bullet Time', character2)
print(character2.currentHealth)
character2.castAbility("Star Call", character2)
print(character2.currentHealth)
print(character2.currentMana)
character2.castAbility("Star Call", character2)
