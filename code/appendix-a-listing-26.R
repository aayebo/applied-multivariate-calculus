flux_integrand <- function(t) {
  nx <- cos(t); ny <- sin(t)
  Gx <- cos(t); Gy <- sin(t)
  Gx*nx + Gy*ny
}
integrate(flux_integrand, 0, 2*pi)$value
