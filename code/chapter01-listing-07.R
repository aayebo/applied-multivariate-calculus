vec_norm <- function(v) sqrt(sum(v^2))
dot <- function(u, v) {
  stopifnot(length(u) == length(v))
  sum(u * v)
}
cross3 <- function(u, v) {
  stopifnot(length(u) == 3, length(v) == 3)
  c(u[2]*v[3] - u[3]*v[2],
    u[3]*v[1] - u[1]*v[3],
    u[1]*v[2] - u[2]*v[1])
}
project <- function(v, onto) {
  d <- dot(onto, onto)
  if (d == 0) stop("Projection onto zero vector")
  dot(v, onto) / d * onto
}
u <- c(2, -1, 2); v <- c(1, 3, -2)
print(vec_norm(u)); print(dot(u, v))
print(cross3(u, v)); print(project(v, u))
