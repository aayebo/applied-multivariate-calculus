P <- c(2, -1, 0)
Q <- c(4, 3, 5)
direction <- Q - P
point_on_line <- function(t) P + t * direction
point_on_line(0)
point_on_line(0.5)
point_on_line(1)
