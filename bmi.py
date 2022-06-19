class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height**2)

        if not (10 <= self.value <= 40):
            raise ValueError

    def __str__(self):
        return f"{self.value:.2f}"


tanaka_bmi = BMI(height=1.8, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print(tanaka_bmi)
print(sasami_bmi)
""" BMIはBMIクラスになる。heightとweightはインスタンス変数 calaculate()はインスタンス・メソッドこれらは抽象
一番したのところで
 """
