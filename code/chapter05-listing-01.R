inner <- function(x) vapply(x,function(xx)
  integrate(function(y) xx+2*y,0,1-xx)$value,numeric(1))
I <- integrate(inner,0,1)$value
print(c(numerical=I,exact=1/2))
stopifnot(abs(I-.5)<1e-8)
