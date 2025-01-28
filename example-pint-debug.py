import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

g = Q_(9.8,'m/s')

def fall_time(h):
    t = (2*h/g)**0.5
    return  t


for h in [1,2,3]:
    h = Q_(h,'m')
    t = fall_time(h)
    print( f"Fall time for object dropped from {h}:", t)
    print( f"                                      ", t.to('s'))
    print( f"                                      ", t.to('ms'))
