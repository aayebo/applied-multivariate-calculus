t <- seq(0, 4*pi, length.out = 500)
x <- cos(t); y <- sin(t); z <- t/4
plot(x, y, type = "l", asp = 1,
     xlab = "x(t)", ylab = "y(t)",
     main = "Projection of a helix onto the xy-plane")
plot(t, z, type = "l", xlab = "t", ylab = "z(t)",
     main = "Vertical coordinate of the helix")
