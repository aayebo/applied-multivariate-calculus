a <- 2
integrand <- function(t) a^2 + 0*t
circulation <- integrate(integrand, 0, 2*pi)$value
area_side <- 2*pi*a^2
print(c(boundary=circulation, interior=area_side))
stopifnot(abs(circulation-area_side)<1e-8)
