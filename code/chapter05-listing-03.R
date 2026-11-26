M <- integrate(function(x) 1+x,0,2)$value
Mx <- integrate(function(x) x*(1+x),0,2)$value
print(c(mass=M,xbar=Mx/M,ybar=.5))
vol <- integrate(function(r) 2*pi*(4-r^2)*r,0,2)$value
print(c(paraboloid_volume=vol,exact=8*pi))
