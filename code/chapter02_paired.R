# Chapter 2: paired mathematical computations in base R
# Figure: helix projections
t <- seq(0,6*pi,length.out=500)
x <- 2*cos(t); y <- 2*sin(t); z <- t/3
par(mfrow=c(1,2))
plot(x,y,type='l',asp=1,xlab='x',ylab='y',main='Top view')
plot(t,z,type='l',xlab='t',ylab='z',main='Height')
par(mfrow=c(1,1))
deriv1 <- function(f,t,h=1e-5) (f(t+h)-f(t-h))/(2*h)
r <- function(t) c(t^2,3*t,2)
stopifnot(max(abs(deriv1(r,2)-c(4,3,0)))<1e-7)
a <- 2; b <- 1/3
L_num <- integrate(function(t) sqrt(a*a+b*b)+0*t,0,2*pi)$value
L_exact <- 2*pi*sqrt(a*a+b*b)
stopifnot(abs(L_num-L_exact)<1e-10)
kappa <- a/(a*a+b*b); tau <- b/(a*a+b*b)
stopifnot(abs(kappa-18/37)<1e-12,abs(tau-3/37)<1e-12)
x <- 3; y <- 4; z <- 5
r_cyl <- sqrt(x*x+y*y); theta <- atan2(y,x)
rho <- sqrt(x*x+y*y+z*z); phi <- acos(z/rho)
stopifnot(abs(rho*sin(phi)*cos(theta)-x)<1e-12)
area <- integrate(function(r) 2*pi*r*sqrt(1+4*r*r),0,1)$value
exact <- pi*(5^(3/2)-1)/6
stopifnot(abs(area-exact)<1e-10)
print(c(arc_length=L_num,curvature=kappa,torsion=tau,area=area))
