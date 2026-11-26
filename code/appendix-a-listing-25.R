integrand <- function(t) {
  x <- cos(t); y <- sin(t)
  Fx <- -y; Fy <- x
  dx <- -sin(t); dy <- cos(t)
  Fx*dx + Fy*dy
}
c(numerical = integrate(integrand, 0, 2*pi)$value,
  exact = 2*pi)
