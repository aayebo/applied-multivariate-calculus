f <- function(x,y) exp(x*y)+x^3*y
fx <- function(x,y) y*exp(x*y)+3*x^2*y
fy <- function(x,y) x*exp(x*y)+x^3
partial <- function(f,x,y,axis="x",h=1e-5) {
  if (axis=="x") (f(x+h,y)-f(x-h,y))/(2*h)
  else (f(x,y+h)-f(x,y-h))/(2*h)
}
print(c(exact_x=fx(1,.5),numeric_x=partial(f,1,.5),
        exact_y=fy(1,.5),numeric_y=partial(f,1,.5,"y")))
