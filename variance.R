
#Zero variance

library(readr)

data <-read.csv("C:\\Users\\hp\\Desktop\\DataSets\\Data praprocessing\\Z_dataset.csv")

data <- data[-c(1,6)]

attach(data)

summary(data)
str(data)

apply(data, 2, var)

which(apply(data, 2, var)==0)
