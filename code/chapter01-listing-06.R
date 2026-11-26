plane_distance <- function(Q, n, d) {
  if (norm3(n) == 0) stop("Plane normal must be nonzero")
  abs(dot3(Q, n) - d) / norm3(n)
}
plane_distance(c(2, 1, 4), c(2, -1, 2), 3)
