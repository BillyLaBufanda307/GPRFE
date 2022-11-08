import gprpy.gprpy as gp
import os
mygpr = gp.gprpyProfile()

iteratedt1 = []

for path in os.listdir('D:/shitgpr/gridtest2/Lineset'):
    if path.endswith(".DT1"):
        iteratedt1.append('D:/shitgpr/gridtest2/Lineset/' + path)
        print(iteratedt1)
    else:
        print("SKIPPING FILE", path)

filename = ""

for file in iteratedt1:
    filename = file[:-3] + "pdf"
    mygpr.importdata(file)
    mygpr.printProfile(filename, color='gray', contrast=10, yrng=[0,60], xrng=[0,5], dpi=600)