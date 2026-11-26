# Chapter 3 paired calculations. Uses base R.
Tfield <- function(x,y) 20+3*x^2+2*y^2
x <- seq(-2,2,length.out=120); y <- seq(-2,2,length.out=120)
z <- outer(x,y,Tfield)
pdf('chapter03_paired_temperature_R.pdf',width=6,height=5)
contour(x,y,z,levels=c(22,24,26,30,34),xlab='x (m)',ylab='y (m)')
dev.off()
stopifnot(Tfield(1,-2)==31)
f <- function(x,y) exp(x*y)+x^3*y
fx <- function(x,y) y*exp(x*y)+3*x^2*y
fy <- function(x,y) x*exp(x*y)+x^3
partial <- function(f,x,y,axis='x',h=1e-5) {
  if (axis=='x') (f(x+h,y)-f(x-h,y))/(2*h)
  else (f(x,y+h)-f(x,y-h))/(2*h)
}
stopifnot(abs(partial(f,1,.5)-fx(1,.5))<1e-8)
h <- function(x,y) x*y/(x^2+y^2)
t <- 10^(-seq(1,6))
print(data.frame(t=t,axis=h(t,0),diagonal=h(t,t)))
J <- function(u,v) matrix(c(2*u,2*v,-2*v,2*u),2,2)
stopifnot(abs(det(J(1,2))-20)<1e-10)
Rg <- 8.314; n <- 1; V <- .025; Temp <- 300
P <- function(v,t) n*Rg*t/v
dV <- .0001; dT <- 2
linear <- (-n*Rg*Temp/V^2)*dV+(n*Rg/V)*dT
actual <- P(V+dV,Temp+dT)-P(V,Temp)
stopifnot(abs(linear-266.048)<1e-8, abs(actual-linear)<10)
print(c(predicted=linear,actual=actual,error=actual-linear))
