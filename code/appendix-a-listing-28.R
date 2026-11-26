great_circle <- function(u, v, radius = 1) {
  u <- u/sqrt(sum(u^2)); v <- v/sqrt(sum(v^2))
  d <- sum(u*v)
  radius * acos(max(-1, min(1, d)))
}
great_circle(c(1,0,0), c(0,1,0), radius = 6371)
