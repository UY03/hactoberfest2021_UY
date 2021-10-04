feet=0
e_inches=0
def inches_to_feet(inches):
    feet = inches // 12
    e_inches = inches % 12
    print("The equivalent is",feet,"Feet and",e_inches,"Inches")

inches_to_feet(77)
inches_to_feet(452)