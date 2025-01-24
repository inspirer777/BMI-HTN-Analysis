# Logistic Regression and Chi-Square Analysis

# Load data
D <- file.choose()
data <- read.table(D, header = TRUE)

# Preprocessing
data[, 1] <- data[, 1] + 3
attach(data)

# Converting columns to factors
AH <- as.factor(AH)
Work <- as.factor(Work)
RO <- as.factor(RO)
age <- as.factor(age)
Rs <- as.factor(Rs)

# Chi-Square Tests
T1 <- table(Rs, AH)
print("Chi-Square Test for Rs and AH:")
print(chisq.test(T1))

T2 <- table(Rs, Work)
print("Chi-Square Test for Rs and Work:")
print(chisq.test(T2))

T3 <- table(Rs, RO)
print("Chi-Square Test for Rs and RO:")
print(chisq.test(T3))

T4 <- table(Rs, age)
print("Chi-Square Test for Rs and Age:")
print(chisq.test(T4))

# Logistic Regression Model
M <- glm(Rs ~ AH + Work + RO + age + Nbr, family = binomial(link = "logit"))
print("Logistic Regression Model Summary (M):")
print(summary(M))

# Adjusting Reference Level for RO
RO <- factor(RO, labels = c("Rent", "Own"))
RO2 <- relevel(RO, ref = "Rent")

# Updated Logistic Regression Model
M2 <- glm(Rs ~ AH + Work + RO2 + age + Nbr, family = binomial(link = "logit"))
print("Updated Logistic Regression Model Summary (M2):")
print(summary(M2))

# Extracting Model Coefficients and Odds Ratios
coefficients <- coef(M2)
odds_ratios <- exp(coefficients)
inverse_odds <- 1 / exp(coefficients)
confidence_intervals <- confint(M2)
odds_confidence_intervals <- exp(confidence_intervals)

# Results
print("Model Coefficients:")
print(coefficients)

print("Odds Ratios:")
print(odds_ratios)

print("Inverse Odds Ratios:")
print(inverse_odds)

print("Confidence Intervals:")
print(confidence_intervals)

print("Odds Ratios Confidence Intervals:")
print(odds_confidence_intervals)

# Backward Selection using AIC
backAIC <- step(M2, direction = "backward", data = data)
print("Backward Selection Model Summary:")
print(summary(backAIC))
