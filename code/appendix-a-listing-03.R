v <- c(2, -1, 4)
w <- c(1, 3, -2)
v[1]                      # first component: R indexes from 1
v[2:3]                    # second and third components
length(v)                 # number of entries
v + w                     # componentwise addition
3 * v                     # scalar multiplication
sum(v * w)                # dot product
sqrt(sum(v^2))            # Euclidean norm
