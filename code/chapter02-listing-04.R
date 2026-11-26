x <- 3; y <- 4; z <- 5
r <- sqrt(x*x+y*y); theta <- atan2(y,x)
rho <- sqrt(x*x+y*y+z*z); phi <- acos(z/rho)
print(c(r=r,theta=theta,z=z,rho=rho,phi=phi))
