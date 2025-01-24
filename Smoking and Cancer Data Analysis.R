# China Example (30/08/1401)

# Define city names
cities <- c("Beijing", "Shanghai", "Shenyang", "Nanjing", 
            "Harbin", "Zhengzhou", "Taiyuan", "Nanchang")

# Define factors for City, Smoker, and Cancer
City <- factor(rep(cities, rep(4, length(cities))), levels = cities)
Smoker <- factor(rep(rep(c("Yes", "No"), c(2, 2)), 8), levels = c("Yes", "No"))
Cancer <- factor(rep(c("Yes", "No"), 16), levels = c("Yes", "No"))

# Count data
count <- c(126, 100, 35, 61, 908, 688, 497, 807, 
           913, 747, 336, 598, 235, 172, 58, 121, 
           402, 308, 121, 215, 182, 156, 72, 98, 
           60, 99, 11, 43, 104, 89, 21, 36)

# Create data frame
chismoke <- data.frame(City, Smoker, Cancer, count)
print("ChiSmoke Data Frame:")
print(chismoke)

# Create contingency table
x <- tapply(count, list(Smoker, Cancer, City), c)
names(dimnames(x)) <- c("Smoker", "Cancer", "City")

# Display the contingency table using flat table format
print("Flat Table Format:")
print(ftable(x, row.vars = c("City", "Smoker"), col.vars = "Cancer"))

# Perform Mantel-Haenszel Chi-Square Test
print("Mantel-Haenszel Chi-Square Test Result:")
mantel_test <- mantelhaen.test(x)
print(mantel_test)
