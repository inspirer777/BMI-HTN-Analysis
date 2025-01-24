# BMI and Hypertension Analysis

# Load data
D <- file.choose()  # Prompt user to select file
dataBMI <- read.table(D, header = TRUE)
head(dataBMI)

# Attach dataset for direct access to columns
attach(dataBMI)

# Calculate BMI and categorize it
BMI <- WEIGHT / (HEIGHT / 100)^2
BMI1 <- cut(BMI, breaks = c(0, 25, 29.99, max(BMI)))
BMI1 <- factor(BMI1, labels = c("Normal", "LittleFat", "Fat"))

# Convert variables to factors
SEX <- as.factor(SEX)
EDU <- as.factor(EDUCATION)
EXRCS <- as.factor(EXRCS)
smok <- as.factor(SMOKING)
HTN <- as.factor(HTN)

# Perform Chi-Square tests
T1 <- table(HTN, BMI1)
print("Chi-Square Test for HTN and BMI:")
print(chisq.test(T1))

T2 <- table(HTN, EDU)
print("Chi-Square Test for HTN and Education:")
print(chisq.test(T2))

T3 <- table(HTN, SEX)
print("Chi-Square Test for HTN and Sex:")
print(chisq.test(T3))

# Logistic regression model
M <- glm(HTN ~ SEX + EDU + EXRCS + smok + BMI1, family = binomial(link = "logit"))
print("Logistic Regression Model 1:")
print(summary(M))

# Relevel SEX variable to set "female" as the reference
sex <- factor(SEX, labels = c("male", "female"))
sex1 <- relevel(sex, ref = "female")

M2 <- glm(HTN ~ sex1 + EDU + EXRCS + smok + BMI1, family = binomial(link = "logit"))
print("Logistic Regression Model 2:")
print(summary(M2))

# Model coefficients and odds ratios
print("Model Coefficients:")
print(coef(M2))

print("Odds Ratios:")
print(exp(coef(M2)))

print("Inverse of Odds Ratios:")
print(1 / exp(coef(M2)))

# Confidence intervals for odds ratios
print("Confidence Intervals for Odds Ratios:")
print(exp(confint(M2)))

# Logistic regression with age included
M3 <- glm(HTN ~ sex1 + EXRCS + smok + BMI1 + AGE, family = binomial(link = "logit"))
print("Logistic Regression Model 3:")
print(summary(M3))

# Prediction with a new data point
xNew <- data.frame(sex1 = "male", smok = "1", BMI1 = "Fat", EXRCS = "1", AGE = 59)
print("New Data for Prediction:")
print(xNew)
print("Predicted Probability of HTN:")
print(predict(M3, xNew, type = "response"))
