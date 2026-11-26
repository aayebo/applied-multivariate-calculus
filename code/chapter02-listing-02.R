deriv1 <- function(f,t,h=1e-5) (f(t+h)-f(t-h))/(2*h)
r <- function(t) c(t^2,3*t,2)
deriv1(r,2) # approximately 4, 3, 0
