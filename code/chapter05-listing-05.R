midpoint <- function(n) {
  m <- ((1:n)-0.5)/n
  sum(outer(m,m,function(x,y) x^2+y^2))/n^2
}
for (n in c(4,8,16,32)) {
  err <- abs(midpoint(n)-2/3)
  cat("n =",n,"error =",format(err,digits=8),"\n")
  stopifnot(abs(err-1/(6*n^2))<1e-12)
}
I <- integrate(function(y) y^2*exp(y^3),0,1)$value
stopifnot(abs(I-(exp(1)-1)/3)<1e-10)
