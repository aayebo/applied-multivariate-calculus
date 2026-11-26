P <- function(p) 12*p[1]+10*p[2]-p[1]^2-2*p[2]^2-p[1]*p[2]
fit <- optim(c(1,1),function(p) -P(p),method="BFGS")
print(c(fit$par,benefit=P(fit$par)))
print(c(exact_x=38/7,exact_y=8/7))
