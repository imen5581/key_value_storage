from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        positive_effect = self.base.get_positive_effects()
        return positive_effect

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        return negative_effects

    @abstractmethod
    def get_stats(self):
        self.base.get_stats()


class AbstractPositive(AbstractEffect):

    @abstractmethod
    def get_positive_effects(self):
        self.base.get_positive_effects()


class AbstractNegative(AbstractEffect):

    @abstractmethod
    def get_negative_effects(self):
        self.base.get_negative_effects()


class Berserk(AbstractPositive):

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append('Berserk')
        return positive_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] = stats["Strength"] + 7
        stats["Endurance"] = stats["Endurance"] + 7
        stats["Agility"] = stats["Agility"] + 7
        stats["Luck"] = stats["Luck"] + 7
        stats["Perception"] = stats["Perception"] -3
        stats["Charisma"] = stats["Charisma"] -3
        stats["Intelligence"] = stats["Intelligence"] -3
        stats["HP"] = stats["HP"] + 50
        return stats


class Blessing(AbstractPositive):

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append('Blessing')
        return positive_effects

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Perception"] += 2
        stats["Endurance"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        return stats


class Weakness(AbstractNegative):

    def get_negative_effects(self):
        negative_effect = self.base.get_negative_effects()
        negative_effect.append('Weakness')
        return negative_effect

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] = stats["Strength"] - 4
        stats["Endurance"] = stats["Endurance"] - 4
        stats["Agility"] = stats["Agility"] - 4
        return stats


class EvilEye(AbstractNegative):

    def get_negative_effects(self) -> []:
        negative_effect = self.base.get_negative_effects()
        negative_effect.append('EvilEye')
        return negative_effect

    def get_stats(self) -> {}:
        stats = self.base.get_stats()
        stats["Luck"] = stats["Luck"] - 10
        return stats


class Curse(AbstractNegative):

    def get_negative_effects(self):
        self.negative_effect = self.base.get_negative_effects()
        self.negative_effect.append('Curse')
        return self.negative_effect

    def get_stats(self):
        stats = self.base.get_stats()

        stats["Strength"] -= 2
        stats["Perception"] -= 2
        stats["Endurance"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        return stats


hero = Hero()
curs = EvilEye(hero)
print(curs.get_stats())
# print(cur1.get_negative_effects())
# print(hero.positive_effects)
#
# positive = Berserk(hero)
# print(positive.get_positive_effects())
# print(positive.get_stats())
#
# print('*****************************')
#
# positive = Berserk(Berserk(hero))
# print(positive.get_positive_effects())
# print(positive.get_stats())

# print(hero.get_stats())
#
# for i in range(20):
#     hero = Blessing(hero)
#     print(hero.get_stats())
