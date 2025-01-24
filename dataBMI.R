D<-file.choose()
dataBMI<-read.table(D,header = T)
dataBMI
head(dataBMI)
attach(dataBMI)
BMI<-WEIGHT/(HEIGHT/100)^2
BMI1<-cut(BMI,breaks = c(0,25,29.99,max(BMI)))
BMI1
BMI1<-factor(BMI1,labels = c("Normal","LittleFat","Fat"))
BMI1
SEX<-as.factor(SEX)
EDU<-as.factor(EDUCATION)
EXRCS<-as.factor(EXRCS)
smok<-as.factor(SMOKING )
HTN<-as.factor(HTN)

T1<-table(HTN,BMI1)
chisq.test(T1)

T2<-table(HTN,EDU)
T2
chisq.test(T2)

T3<-table(HTN,SEX)
T3
chisq.test(T3)
###########B#######
M<-glm(HTN~SEX+EDU+EXRCS+smok+BMI1,family = binomial(link = "logit"))
M
summary(M)
sex<-factor(SEX,labels = c("male","female"))
sex
sex1<-relevel(sex,ref = "female")
sex1
M2<-glm(HTN~sex1+EDU+EXRCS+smok+BMI1,family = binomial(link = "logit"))
M2
summary(M2)

coef(M2)
exp(coef(M2))
1/exp(coef(M2))
confint(M2)

exp(confint(M2))


M3<-glm(HTN~sex1+EXRCS+smok+BMI1+AGE,family = binomial(link = "logit"))
M3
summary(M3)
xNew<-data.frame(sex1="male",smok="1",BMI1="Fat",EXRCS="1",AGE=59)
xNew
predict(M3,xNew,type = "response")
