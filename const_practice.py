class planet:
    def __init__(self,name='Earth'):
        self.speed=10
        self.name=name
        self.distance=1000
earth=planet()
print(earth.name)