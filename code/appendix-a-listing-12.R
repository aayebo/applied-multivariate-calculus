x <- seq(-2, 2, length.out = 81)
y <- seq(-2, 2, length.out = 81)
z <- outer(x, y, function(a, b) a^2 + b^2)
contour(x, y, z, xlab = "x", ylab = "y",
        main = "Level curves of z = x^2 + y^2")
persp(x, y, z, theta = 35, phi = 25,
      xlab = "x", ylab = "y", zlab = "z",
      main = "Paraboloid")
