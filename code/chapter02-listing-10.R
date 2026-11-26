area_fun <- function(r) 2*pi*r*sqrt(1+4*r^2)
area_num <- integrate(area_fun, lower=0, upper=1)$value
area_exact <- pi*(5^(3/2)-1)/6
stopifnot(abs(area_num-area_exact)<1e-8)
print(c(numerical=area_num, exact=area_exact))
