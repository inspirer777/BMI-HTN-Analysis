### china example 30/08/1401
cities<-
  c("Beijing","Shanghai","Shenyang","Nanjing","Harbin","Zhengzhou","Taiyuan","Nanchang")
City<-factor(rep(cities,rep(4,length(cities))),levels=cities)
Smoker<-factor(rep(rep(c("Yes","No"),c(2,2)),8),levels=c("Yes","No"))
Cancer<-factor(rep(c("Yes","No"),16),levels=c("Yes","No"))
count<-c(126,100,35,61,908,688,497,807,913,747,336,598,235,172,58,
         121,402,308,121,215,182,156,72,98,60,99,11,43,104,89,21,36)
chismoke<-data.frame(City,Smoker,Cancer,count)
chismoke
x<-tapply(count,list(Smoker,Cancer,City),c)
names(dimnames(x))<-c("Smoker","Cancer","City")
ftable(x,row.vars=c("City","Smoker"),col.vars="Cancer")
mantelhaen.test(x)
