x <- seq(-2, 2, length.out = 101)
y <- seq(-2, 2, length.out = 101)
z <- x^2 + 2*x + 1
head(z)
G <- expand.grid(x = seq(-1, 1, by = 0.5),
                 y = seq(-1, 1, by = 0.5))
G$height <- G$x^2 + G$y^2
head(G)
