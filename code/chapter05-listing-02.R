inner <- function(x) vapply(x,function(xx)
  integrate(function(y) 2+.5*xx+y^2,0,2)$value,numeric(1))
E <- integrate(inner,0,3)$value
print(c(total=E,average=E/6,exact=49/2))
