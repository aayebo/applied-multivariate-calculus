rhs <- function(z) {
  r <- z[1]; vr <- z[3]; vt <- z[4]
  c(vr, vt, r*vt^2, -2*vr*vt/r)
}
rk4 <- function(n) {
  h <- 1/n; z <- c(1,0,0,1)
  err <- 0
  for (i in seq_len(n)) {
    k1 <- rhs(z)
    k2 <- rhs(z + h*k1/2)
    k3 <- rhs(z + h*k2/2)
    k4 <- rhs(z + h*k3)
    z <- z + h*(k1+2*k2+2*k3+k4)/6
    t <- i*h
    err <- max(err,abs(z[1]*cos(z[2])-1),
               abs(z[1]*sin(z[2])-t))
  }
  err
}
print(sapply(c(20,40,80,160),rk4))
