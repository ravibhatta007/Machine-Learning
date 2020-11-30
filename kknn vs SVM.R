cat("\014") # Clearing of the console
rm(list = ls())  #clear environment
library(kknn)
library(kernlab)
data <- read.table("credit_card_data-headers.txt",header=TRUE)
head(data)
set.seed(1)
#60% for training -- "sample" selects a sample of data points
train_row = sample(nrow(data), size = floor(nrow(data) * 0.6))
train_data = data[train_row,]  # training data set

#Using the remaining data for test and validation split

remaining = data[-train_row, ] 
val_row = sample(nrow(remaining), size = floor(nrow(remaining)/2))
val_data = remaining[val_row,]  # validation data set
test_data = remaining[-val_row, ] #test data set
accuracy<-rep(0,35)
#generate 10 different model of SVM with 10 different values of C
#c_val = 1e-6 * 100 ^ (1:10-1)
c_val=c(1,3)
for (i in 1:length(c_val)) {
  
  # fit model using training set
  
  model_scaled <- ksvm(as.matrix(train_data[,1:10]),
                       as.factor(train_data[,11]),
                       type = "C-svc", # Use C-classification method
                       kernel = "vanilladot", # Use simple linear kernel
                       C = c_val[i],
                       scaled=TRUE) 
  #  compare models using validation set
  
  pred <- predict(model_scaled,val_data[,1:10])
  accuracy[i] = sum(pred == val_data$R1) / nrow(val_data)
}

accuracy[1:10]
Best_C=c_val[which.max(accuracy[1:10])]

# Using the C value with highest accuracy to test data
     model_scaled <- ksvm(as.matrix(train_data[,1:10]),
              as.factor(train_data[,11]),
		          type = "C-svc", # Use C-classification method
              kernel = "vanilladot", # Use simple linear kernel
              C = c_val[which.max(accuracy[1:10])], # from above ksvm calculation
		   scaled=TRUE) # have ksvm scale the data for you

pred2=predict(model_scaled,test_data[,1:10])
Test_accuracy_ksvm=sum(pred2 == test_data$R1) / nrow(test_data)

for (k in 1:25) {
  
  # fit k-nearest-neighbor model using training set, validate on test set
  
  knn_model <- kknn(R1~.,train_data,val_data,k=k,scale=TRUE)
  
  #  compare models using validation set
  
  pred <- round(fitted(knn_model))  # Converting to 0 or 1 result
  accuracy[k+10] = sum(pred == val_data$R1) / nrow(val_data)
}

Best_k=which.max(accuracy[11:35])

# Testing best model with test data 
knn_model <- kknn(R1~.,train_data,test_data,
                  k=12,
                  scale=TRUE)

pred <- round(fitted(knn_model)) # round off to 0 or 1

kknn_test_accuracy=sum(pred == test_data$R1) / nrow(test_data)

if (Test_accuracy_ksvm>kknn_test_accuracy){ 
  cat('Best model is KSVM with C =',Best_C)
  } else{
  cat('Best model is KKNN with k =',Best_k)
  }


