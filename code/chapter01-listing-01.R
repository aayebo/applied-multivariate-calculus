P <- c(1, -2, 4)
Q <- c(5, 1, -2)
displacement <- Q - P
distance <- sqrt(sum(displacement^2))
midpoint <- (P + Q) / 2
print(displacement)
print(distance)
print(midpoint)
