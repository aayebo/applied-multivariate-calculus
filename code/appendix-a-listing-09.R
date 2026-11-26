classify <- function(x) {
  if (x > 0) {
    "positive"
  } else if (x < 0) {
    "negative"
  } else {
    "zero"
  }
}
for (k in 1:4) {
  cat("k =", k, "; k squared =", k^2, "\n")
}
