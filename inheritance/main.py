# class Animal:
#     def __init__(self):
#         self.num_of_eyes = 2
#
#     def breathe(self):
#         print("inhale,exhale")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#
#     def swim(self):
#         print("moving in water")
#
#
# nemo = Fish()
# # nemo.swim()
# nemo.breathe()
# # print(nemo.num_of_eyes)
from array import *
vals = array('i',[3,4,2,1])
print(vals)
print(vals.buffer_info())