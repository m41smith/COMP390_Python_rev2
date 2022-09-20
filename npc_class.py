from character_class import Character


class Npc(Character):
    def __init__(self, typ, health_pts, wp, dr, df, exp, sts, voc):
        super().__init__()
        self.type = typ
        self.hp = health_pts
        self.weapon = wp
        self.drop = dr
        self.defence_factor = df
        self.xp = exp
        self.stats = sts
        self.vocalization = voc

    def get_hp(self):
        return self.hp

    def speak(self):
        print(self.vocalization)

    def take_damage(self, damage_amount):
        self.hp -= damage_amount
