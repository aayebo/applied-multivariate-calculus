J <- function(u,v) matrix(c(2*u,2*v,-2*v,2*u),2,2)
print(det(J(1,2)))
Rg <- 8.314; n <- 1; V <- .025; Temp <- 300
P <- function(v,t) n*Rg*t/v
dV <- .0001; dT <- 2
linear <- (-n*Rg*Temp/V^2)*dV + (n*Rg/V)*dT
actual <- P(V+dV,Temp+dT)-P(V,Temp)
print(c(predicted=linear,actual=actual,error=actual-linear))
