q <- function(x) x^2 + 2*(6-x)^2
answer <- optimize(q, c(0, 6))
x_star <- answer$minimum
y_star <- 6 - x_star
c(x = x_star, y = y_star, objective = answer$objective)
