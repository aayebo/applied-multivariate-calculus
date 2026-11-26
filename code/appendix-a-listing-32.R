check_close <- function(actual, expected, tol = 1e-7) {
  stopifnot(is.numeric(actual), is.numeric(expected))
  stopifnot(length(actual) == length(expected))
  stopifnot(all(is.finite(actual)), all(is.finite(expected)))
  stopifnot(max(abs(actual - expected)) < tol)
  invisible(TRUE)
}
check_close(sum(c(1,2,3)*c(4,5,6)), 32)
