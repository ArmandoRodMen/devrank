import math as math

width_cm= 33.87
height_cm= 19.05

width_px= 1280
height_px= 720

aspectRatio= width_cm/height_cm
aspectRatio_px= width_px/height_px

print(aspectRatio,"cm ")
print(aspectRatio_px,"px ")

workSpace_Width_px= width_px
workSpace_Height_px= workSpace_Width_px/aspectRatio_px

print("Width= ", workSpace_Width_px, "px, Height= ", workSpace_Height_px, "px")

baro_1_Diameter= 21
baro_5_Diameter= 25
baro_10_Diameter= 28

baro_1_Radius= baro_1_Diameter/2
baro_5_Radius= baro_5_Diameter/2
baro_10_Radius= baro_10_Diameter/2

baro_1_Area= (math.pi)*((baro_1_Radius**2))
baro_5_Area= (math.pi)*((baro_5_Radius**2))
baro_10_Area= (math.pi)*((baro_10_Radius**2))

baro_1_Area_px= ((baro_1_Area*width_cm)/workSpace_Width_px)*1000
baro_5_Area_px= ((baro_5_Area*width_cm)/workSpace_Width_px)*1000
baro_10_Area_px= ((baro_10_Area*width_cm)/workSpace_Width_px)*1000

print("1 baro Area px= ", baro_1_Area_px)
print("5 baro Area px= ", baro_5_Area_px)
print("10 baro Area px= ", baro_10_Area_px)
