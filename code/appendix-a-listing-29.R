h <- 0.05
N <- 20
t <- seq(0, N*h, by = h)
y <- numeric(N+1)
y[1] <- 1
for (k in 1:N) {
  y[k+1] <- y[k] - h*y[k]
}
max(abs(y - exp(-t)))
plot(t, y, type = "b", xlab = "t", ylab = "y(t)")
lines(t, exp(-t), lty = 2)
