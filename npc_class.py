
class Npc:
    def __init__(self, typ, health_pts, wp, dr, df, exp, sts, voc):
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

    def set_hp(self, num):
        self.hp = num
