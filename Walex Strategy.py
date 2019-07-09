print("Look at the first 12 squares ahead of you on the game board. ")

print("Analyze which colored square(s) most frequently show up within the 12-square range. ")

print("Enter the number of squares for each color in the range: ")
print("Input Yellow: ")
y = input()
print("Input Blue: ")
b = input()
print("Input Green: ")
g = input()
print("Input Red: ")
r = input()
print("Input Orange: ")
o = input()

if y > (b or g or r or o):
    print("My suggestion to you is to base your allocations more on YELLOW")
if b > (y or g or r or o):
    print("My suggestion to you is to base your allocations more on BLUE")
if g > (y or b or r or o):
    print("My suggestion to you is to base your allocations more on GREEN")
if r > (y or b or g or o):
    print("My suggestion to you is to base your allocations more on RED")
if o > (y or b or g or r):
    print("My suggestion to you is to base your allocations more on ORANGE")

print("Enter the asset values for all Event Cards")
print("Input Yellow Card Assets: ")
print("Asset Value For Stocks: ")
S1 = input()
print("Asset Value For Bonds: ")
B1 = input()
print("Asset Value For Currency: ")
X1 = input()
print("Asset Value For Commodities: ")
C1 = input()
print("Asset Value For Real Estate: ")
R1 = input()

print("Input Blue Card Assets: ")
print("Asset Value For Stocks: ")
S2 = input()
print("Asset Value For Bonds: ")
B2 = input()
print("Asset Value For Currency: ")
X2 = input()
print("Asset Value For Commodities: ")
C2 = input()
print("Asset Value For Real Estate: ")
R2 = input()

print("Input Green Card Assets: ")
print("Asset Value For Stocks: ")
S3 = input()
print("Asset Value For Bonds: ")
B3 = input()
print("Asset Value For Currency: ")
X3 = input()
print("Asset Value For Commodities: ")
C3 = input()
print("Asset Value For Real Estate: ")
R3 = input()

print("Input Red Card Assets: ")
print("Asset Value For Stocks: ")
S4 = input()
print("Asset Value For Bonds: ")
B4 = input()
print("Asset Value For Currency: ")
X4 = input()
print("Asset Value For Commodities: ")
C4 = input()
print("Asset Value For Real Estate: ")
R4 = input()

print("Input Orange Card Assets: ")
print("Asset Value For Stocks: ")
S5 = input()
print("Asset Value For Bonds: ")
B5 = input()
print("Asset Value For Currency: ")
X5 = input()
print("Asset Value For Commodities: ")
C5 = input()
print("Asset Value For Real Estate: ")
R5 = input()

assetlist = [[y, ":", S1, B1, X1, C1, R1],
             [b, ":", S2, B2, X2, C2, R2],
             [g, ":", S3, B3, X3, C3, R3],
             [r, ":", S4, B4, X4, C4, R4],
             [o, ":", S5, B5, X5, C5, R5], ]
for item in assetlist:
    print(item[0], item[1], item[2], item[3], item[4], item[5], item[6])

ps = [y*S1 + b*S2 + g*S3 + r*S4 + o*S5]
pb = [y*B1 + b*B2 + g*B3 + r*B4 + o*B5]
px = [y*X1 + b*X2 + g*X3 + r*X4 + o*X5]
pc = [y*C1 + b*C2 + g*C3 + r*C4 + o*C5]
pr = [y*R1 + b*R2 + g*R3 + r*R4 + o*R5]
plist = [ps, pb, px, pc, pr]

print("The probability for each asset is: ")
print(plist)

if ps >= (pb and px and pc and pr):
    print("The safest choice is to allocate more chips on Stocks")
if pb >= (ps and px and pc and pr):
    print("The safest choice is to allocate more chips on Bonds")
if px >= (ps and pb and pc and pr):
    print("The safest choice is to allocate more chips on Currency")
if pc >= (ps and pb and px and pr):
    print("The safest choice is to allocate more chips on Commodities")
if pr >= (ps and pb and px and pc):
    print("The safest choice is to allocate more chips on Real Estate")

print("Allocate on your own judgement")
