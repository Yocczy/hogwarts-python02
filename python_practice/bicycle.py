import yaml


class Bicycle():

    def run(self, km):
        print(f'骑行里程为：{km} km')


class EBicycle(Bicycle):

    def __init__(self, battery_level=10):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        self.battery_level = self.battery_level + vol

    def run(self, km):
        self.km = km - self.battery_level * 10

        if self.km > 0:
            print(f'先用电行驶：{self.battery_level * 10} km')
            super().run(self.km)
        else:
            print(f'已经用电行驶：{km} km')


if __name__ == '__main__':
    eb = EBicycle(20)
    eb.run(1000)
    eb.fill_charge(70)
    eb.run(1000)
    eb.fill_charge(10)
    eb.run(1000)
    with open('bicycle.yml') as f:
        datas = yaml.safe_load(f)

    print(datas['e1_level'])
    battery_level = datas['e1_level']['battery_level']
    run_km = datas['e1_level']['run_km']

    eb = EBicycle(battery_level)
    eb.run(run_km)
