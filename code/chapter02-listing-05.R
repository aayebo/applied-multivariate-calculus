area <- integrate(function(r) 2*pi*r*sqrt(1+4*r*r),0,1)$value
exact <- pi*(5^(3/2)-1)/6
print(c(numerical=area, exact=exact))
