# Chapter 5 paired R calculations
inner <- function(x) vapply(x,function(xx) integrate(function(y) xx+2*y,0,1-xx)$value,numeric(1))
I <- integrate(inner,0,1)$value
stopifnot(abs(I-.5)<1e-8)
innerE <- function(x) vapply(x,function(xx) integrate(function(y) 2+.5*xx+y^2,0,2)$value,numeric(1))
E <- integrate(innerE,0,3)$value
stopifnot(abs(E-24.5)<1e-8)
M <- integrate(function(x) 1+x,0,2)$value
Mx <- integrate(function(x) x*(1+x),0,2)$value
stopifnot(abs(M-4)<1e-8,abs(Mx/M-7/6)<1e-8)
vol <- integrate(function(r) 2*pi*(4-r^2)*r,0,2)$value
stopifnot(abs(vol-8*pi)<1e-8)
set.seed(2026);n <- 100000;x <- runif(n);y <- runif(n)
vals <- ifelse(x+y<=1,x+2*y,0)
print(c(triangle=I,exposure=E,mass=M,xbar=Mx/M,volume=vol,MC=mean(vals),MC_SE=sd(vals)/sqrt(n)))
