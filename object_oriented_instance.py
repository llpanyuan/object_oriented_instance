# 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
# 实例1：猫
class Cat:
    eyes = 2
    legs = 4
    attributes = "可爱"

    def catching_mouse(self):
        print("猫会捉老鼠！")

    def coquettish(self):
        print("猫爱撒娇!")


# 实例2：王者荣耀英雄-妲己
class DaJi:
    height = 165
    positioning = "AP"
    statement = "被玩儿坏了。"

    def squat_grass(self):
        print("妲己最擅长的就是蹲草丛了！")

    def spike_others(self):
        self.squat_grass()
        print("一旦被她蹲到你就被秒儿了！！！")


# 实例3：python
class Python:
    writer = "Guido van Rossum"
    famous_words = "人生苦短，我用python"

    def ai(self):
        print("python可以应用在AI领域！")

    def testing(self):
        print("python可以用作测试的脚本语言！")


# 实例4：柯南
class Conan:
    nickname = "平成的福尔摩斯"
    age = 7
    birth_date = 5 / 4
    favorite_words = "真実はいつもひとつ！"

    def play_football(self):
        print("柯南会踢足球！")

    def reasioning(self):
        print("柯南很擅长推理！")

    def speak_english(self):
        print("柯南会说英语！")


# 实例5：地球
class Earth:
    population = "76.6亿"
    satellite = "月球"
    radius = "6371km"

    def rotation(self):
        print("地球会自转，速度为465.1m/s")

    def revolution(self):
        print("地球会公转，速度为29.79km/s")
