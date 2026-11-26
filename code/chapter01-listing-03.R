project_onto <- function(u, v) {
  denom <- dot3(v, v)
  if (denom == 0) stop("Cannot project onto zero vector")
  dot3(u, v) / denom * v
}
F <- c(6, 2, 3)
d <- c(2, 1, 0)
parallel <- project_onto(F, d)
perpendicular <- F - parallel
print(parallel)
print(dot3(perpendicular, d)) # approximately 0
