coordinatesX = []
coordinatesY = []

n=int(input("Enter the number of polygon points:"))
print("Enter x coordinates for polygon points:")

for i in range(0,n):
    a = float(input(""))
    coordinatesX.append(a)

print("Enter y coordinates for polygon points:")

for j in range(0,n):
    e = float(input(""))
    coordinatesY.append(e)

b=0
c=0
area=0.
sx=0.
sy=0.
ix=0.
iy=0.
ixy=0.
xt=0.
yt=0.
ixt=0.
iyt=0.
ixyt=0.

print(f"{'X':>13} {'Y':>6}")
for b in range(0,n):
    c = c + 1
    print(f"{'Point'} {c}   {coordinatesX[b]:.2f}   {coordinatesY[b]:.2f}")

print("Geometric Properties:")

for d in range(0,n-1):
    area=(coordinatesX[d]+coordinatesX[d+1])*(coordinatesY[d]-coordinatesY[d+1])*.5+area
if area<0:
    area=-1*area
else :
    area=area
print(f"{'Ax:':10}{area:>5.2f}")

for g in range(0,n-1):
    sx=(coordinatesX[g+1]-coordinatesX[g])*(coordinatesY[g+1]**2+coordinatesY[g]**2+coordinatesY[g]*coordinatesY[g+1])*(-1/6)+sx
print(f"{'Sx:':10}{sx:>5.2f}")

for h in range(0,n-1):
    sy=(coordinatesY[h+1]-coordinatesY[h])*(coordinatesX[h+1]**2+coordinatesX[h]**2+coordinatesX[h]*coordinatesX[h+1])*(1/6)+sy
print(f"{'Sy:':10}{sy:>5.2f}")

for k in range(0,n-1):
    ix=(coordinatesX[k+1]-coordinatesX[k])*(coordinatesY[k+1]**3+coordinatesY[k+1]**2*coordinatesY[k]+coordinatesY[k+1]*coordinatesY[k]**2+coordinatesY[k]**3)*(-1/12)+ix
print(f"{'Ix:':10}{ix:>5.2f}")

for l in range(0,n-1):
    iy=(coordinatesY[l+1]-coordinatesY[l])*(coordinatesX[l+1]**3+coordinatesX[l+1]**2*coordinatesX[l]+coordinatesX[l+1]*coordinatesX[l]**2+coordinatesX[l]**3)*(1/12)+iy
print(f"{'Iy:':10}{iy:>5.2f}")

for m in range(0,n-1):
    ixy=(coordinatesY[m+1]-coordinatesY[m])*(coordinatesY[m+1]*(3*coordinatesX[m+1]**2+2*coordinatesX[m+1]*coordinatesX[m]+coordinatesX[m]**2)+coordinatesY[m]*(3*coordinatesX[m]**2+2*coordinatesX[m+1]*coordinatesX[m]+coordinatesX[m+1]**2))*(-1/24)+ixy
print(f"{'Ixy:':10}{ixy:>5.2f}")

xt=sy/area
print(f"{'Xt:':10}{xt:>5.2f}")

yt=sx/area
print(f"{'Yt:':10}{yt:>5.2f}")

ixt=ix-(yt**2)*area
print(f"{'Ixt:':10}{ixt:>5.2f}")

iyt=iy-(xt**2)*area
print(f"{'Iyt:':10}{iyt:>5.2f}")

ixyt=ixy+xt*yt*area
print(f"{'Ixyt:':10}{ixyt:>5.2f}")
