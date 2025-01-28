import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


x = Q_(1,'ft')

print(x)
print(x.to("m"))
