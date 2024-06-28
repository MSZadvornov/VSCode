
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy
    
    def display(self):
        print(f"Точка здесь {self.x},{self.y}")
point = Point(0, 0)
point.display()
point.move(5, -3)
point.display()
