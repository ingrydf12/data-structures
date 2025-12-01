# For RPG
import random;

class_type = ["Archer", "Warrior", "Magician"];

class Player:
  def __init__(self, class_type, name):
    self.class_type = class_type;
    self.name = name;

  def __spr__:
    return print(f"{self.name} / Classe: {self.class_type}");
