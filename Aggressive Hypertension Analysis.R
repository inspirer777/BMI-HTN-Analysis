# Aggressive Analysis - Applied Question 7 (Quarter 2)

# Load necessary library
library(readxl)

# Load dataset
prob2 <- read_excel("C:/Users/BEHINLAPTOP/Desktop/~/1401-1402/mohasebat/competition Questions/7/Prob2.xls")
head(prob2)

# Calculate BMI and categorize it
bmi <- prob2$WEIGHT / (prob2$HEIGHT / 100)^2
bmi
bmi1 <- cut(bmi, breaks = c(0, 25, 29.99, max(bmi)))
bmi1 <- factor(bmi1, labels = c("normal", "littlefat", "fat"))
bmi1

# Convert variables to factors
prob2$SEX <- as.factor(prob2$SEX)
prob2$EDUCATION <- as.factor(prob2$EDUCATION)
prob2$EXRCS <- as.factor(prob2$EXRCS)
prob2$SMOKING <- as.factor(prob2$SMOKING)

# Perform Chi-Square tests
t1 <- table(prob2$HTN, bmi1)
print("Chi-Square Test for HTN and BMI:")
print(chisq.test(t1))

t2 <- table(prob2$HTN, prob2$EDUCATION)
print("Chi-Square Test for HTN and Education:")
print(chisq.test(t2))

t3 <- table(prob2$HTN, prob2$SEX)
print("Chi-Square Test for HTN and Sex:")
print(chisq.test(t3))

# Logistic regression model
M <- glm(prob2$HTN ~ prob2$SEX + prob2$EDUCATION + prob2$EXRCS + prob2$SMOKING + bmi1, 
         family = binomial(link = "logit"))
print("Logistic Regression Model 1:")
print(summary(M))

# Relevel SEX variable to change the reference level
prob2$SEX <- factor(prob2$SEX, labels = c("male", "female"))
sex <- relevel(prob2$SEX, ref = "female")

M2 <- glm(prob2$HTN ~ sex + prob2$EDUCATION + prob2$EXRCS + prob2$SMOKING + bmi1, 
          family = binomial(link = "logit"))
print("Logistic Regression Model 2:")
print(summary(M2))

# Model coefficients
print("Model Coefficients:")
print(coef(M2))

# Odds ratios
print("Odds Ratios:")
print(exp(coef(M2)))

# Inverse of odds ratios
print("Inverse of Odds Ratios:")
print(1 / exp(coef(M2)))

# Confidence intervals for odds ratios
print("Confidence Intervals for Odds Ratios:")
print(exp(confint(M2)))

# Model predictions
print("Predicted Values:")
print(predict(M2))
