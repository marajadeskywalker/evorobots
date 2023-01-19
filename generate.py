import pyrosim.pyrosim as pyrosim

x = 2
y = 2
z = 0

length = 1
width = 1
height = 1

pyrosim.Start_SDF("boxes.sdf")
for i in range(5):
    for j in range(5):
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length,width,height])
            z += 1.1
            length *= 0.9
            width *= 0.9
            height *= 0.9
        z = 0
        length = 1
        width = 1
        height = 1
        y -= 1
    x -= 1
    y = 2

pyrosim.End()
