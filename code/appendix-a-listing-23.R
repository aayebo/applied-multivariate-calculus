R <- 2
area <- integrate(function(r) 2*pi*r, 0, R)$value
c(numerical = area, exact = pi*R^2)
