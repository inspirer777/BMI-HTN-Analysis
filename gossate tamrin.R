# 1 
x=7.01
x2=5.99
1-pchisq(7,2)


## naghes

n <- c(676,648)
np <-c(18,28)
p <- prop.test(np,n)
p
p1 <- p$estimate[1]
p2<- p$estimate[2]
p1
p2
D <-p1-p2
D
sigma = sqrt(p1*(1-p1)/n[1]+p2*(1-p2)/n[2])
sigma
u = (p1-p2)+qnorm(0.975)*sigma
L = (p1-p2)-qnorm(0.975)*sigma
u
L


## example jozve 2 
x <- c(189,104)
n <-c(11034,11037)
p <- prop.test(x,n)
p1 <- p$estimate[1]
p2<- p$estimate[2]
RR <-p1/p2
RR
L1<- exp(((log(p1/p2))-qnorm(0.975)*sqrt((1-p1)/(n[1]*p1)+(1-p2)/(n[2]*p2))))
L1
u1 <- exp(((log(p1/p2))+qnorm(0.975)*sqrt((1-p1)/(n[1]*p1)+(1-p2)/(n[2]*p2))))
u1
