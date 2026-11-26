value <- integrate(function(x) x^2, 0, 1)$value
exact <- 1/3
cat("Integral of x^2 on [0,1]\n")
cat("  Numerical estimate:", sprintf("%.8f", value), "\n")
cat("  Exact value:      1/3\n")
cat("  Absolute error:  ", sprintf("%.2e", abs(value-exact)),
    "\n")
