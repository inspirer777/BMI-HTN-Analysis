# Chi-Square Test and Proportion Analysis

# Example 1: Chi-Square Calculation
x <- 7.01
x2 <- 5.99
chi_square_prob <- 1 - pchisq(7, 2)
print("Chi-Square Probability:")
print(chi_square_prob)

# Example 2: Proportion Test with Differences

# Observed data
n <- c(676, 648)  # Total sample sizes
np <- c(18, 28)   # Number of successes

# Perform proportion test
p <- prop.test(np, n)
print("Proportion Test Results:")
print(p)

# Extract proportion estimates
p1 <- p$estimate[1]
p2 <- p$estimate[2]
D <- p1 - p2  # Difference between proportions

# Calculate standard error and confidence intervals
sigma <- sqrt(p1 * (1 - p1) / n[1] + p2 * (1 - p2) / n[2])
u <- D + qnorm(0.975) * sigma  # Upper limit
L <- D - qnorm(0.975) * sigma  # Lower limit

# Results
print("Proportion Difference:")
print(D)
print("Confidence Interval for Difference:")
print(c(L, u))

# Example 3: Relative Risk Analysis

# Data for proportions
x <- c(189, 104)   # Number of successes
n <- c(11034, 11037)  # Total sample sizes

# Perform proportion test
p <- prop.test(x, n)

# Extract proportions
p1 <- p$estimate[1]
p2 <- p$estimate[2]

# Relative Risk (RR)
RR <- p1 / p2

# Calculate confidence intervals for RR
L1 <- exp(log(RR) - qnorm(0.975) * sqrt((1 - p1) / (n[1] * p1) + (1 - p2) / (n[2] * p2)))
u1 <- exp(log(RR) + qnorm(0.975) * sqrt((1 - p1) / (n[1] * p1) + (1 - p2) / (n[2] * p2)))

# Results
print("Relative Risk (RR):")
print(RR)
print("Confidence Interval for RR:")
print(c(L1, u1))
