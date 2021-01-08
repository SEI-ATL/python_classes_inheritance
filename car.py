# class

class Car():
  """ This is a car class that will display the make, model, and color """
  
  def __init__(self, make, model, color):
    self.make = make
    self.model = model
    self.color = color
    self.gas = 100
  
  def __str__(self):
    return "{}, {}, {}".format(self.make, self.model, self.color)
  
  def drive(self):
    self.gas -= 10
    
  def fill_tank(self):
    self.gas = 100
    
  def check_gas(self):
    print(f"Gas handle: {self.gas}")

car1 = Car('Mercedes', 'C300', 'white')

car1.drive() # equal to 90
car1.drive() # equal to 80
car1.check_gas()
car1.fill_tank()
car1.check_gas()

class Zoom():
    def __init__(self, computer, software, working):
        self.computer = computer
        self.software = software
        self.working = working
    
    def __str__(self):
        return f"Zoom is not working with my {self.computer}"
    
    def switch_computer(self):
        print('Switched to my other mac')
    
    def use_zoom_on_firefox(self):
        print(f"Zoom is lagging on my {self.computer}")
    
    def use_zoom_on_chrome(self):
        print(f"Zoom is not working well on my computer")
        
rome_computer = Zoom('Macbook', 'Updated Version', False)
rome_computer.switch_computer()
rome_computer.use_zoom_on_chrome()
rome_computer.use_zoom_on_firefox()