class slave:
  injured = 564
  age = 42
  height = 20
  
  def get_older(self):
    self.age += 1
  
my_slave = slave()

print(my_slave.age)

my_slave.get_older()

print(my_slave.age)



