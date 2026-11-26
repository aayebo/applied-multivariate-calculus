d <- c(4, -2, 5)
n <- c(2, 1, -2)
normal_component <- sum(d*n)/sqrt(sum(n^2))
projection <- (sum(d*n)/sum(n^2))*n
tangent_component <- d - projection
cat("Normal scalar component:", normal_component, "\n")
cat("Normal projection:", projection, "\n")
cat("Tangential component:", tangent_component, "\n")
stopifnot(abs(sum(tangent_component*n)) < 1e-10)
stopifnot(max(abs(projection+tangent_component-d)) < 1e-10)
