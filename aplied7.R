## agggressieve
### applied 7 Q2
library(readxl)
prob2 <- read_excel("C:/Users/BEHINLAPTOP/Desktop/~/1401-1402/mohasebat/competition Questions/7/Prob2.xls")
head(prob2)
bmi = prob2$WEIGHT/(prob2$HEIGHT/100)^2
bmi
bmi1 = cut(bmi,breaks=c(0,25,29.99,max(bmi)))
bmi1 <- factor(bmi1,labels = c("normal","littlefat","fat"))
bmi1
prob2$SEX = as.factor(prob2$SEX)
prob2$SEX
prob2$EDUCATION = as.factor(prob2$EDUCATION )
prob2$EXRCS = as.factor(prob2$EXRCS)
prob2$SMOKING = as.factor(prob2$SMOKING)

t1 = table(prob2$HTN,bmi1)
chisq.test(t1)

t2 = table(prob2$HTN,prob2$EDUCATION)
chisq.test(t2)

t3 = table(prob2$HTN,prob2$SEX)
chisq.test(t3)

M = glm(prob2$HTN~prob2$SEX+prob2$EDUCATION+prob2$EXRCS+prob2$SMOKING+bmi1,family = binomial(link = "logit") )
M
summary(M)
prob2$SEX <- factor(prob2$SEX,labels = c("male","female"))
###### change men and women
sex = relevel(prob2$SEX,ref = "female")
sex

M2 = glm(prob2$HTN~sex+prob2$EDUCATION+prob2$EXRCS+prob2$SMOKING+bmi1,family = binomial(link = "logit") )
M2
summary(M2)
## zarib model

####### kamtar az 1 memishe tahlil shavad bayad aks shavad 
coef(M2)
####### ods.ratio
exp(coef(M2))
###### aks
1/exp(coef(M2))

confint(M2)
## fase etminan nesbat bakht ha 
exp(confint(M2))

predict(M2)


