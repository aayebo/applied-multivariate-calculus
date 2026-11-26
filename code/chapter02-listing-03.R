a <- 2; b <- 1/3
speed <- function(t) sqrt(a*a+b*b)+0*t
L_num <- integrate(speed,0,2*pi)$value
L_exact <- 2*pi*sqrt(a*a+b*b)
kappa <- a/(a*a+b*b); tau <- b/(a*a+b*b)
print(c(length=L_num, error=abs(L_num-L_exact),
        curvature=kappa, torsion=tau))
