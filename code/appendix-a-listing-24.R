set.seed(2026)
n <- 100000
x <- runif(n); y <- runif(n)
values <- x^2 + y^2
estimate <- mean(values)
mc_se <- sd(values)/sqrt(n)
c(estimate = estimate, SE = mc_se, exact = 2/3)
