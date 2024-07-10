if (!requireNamespace("evclass", quietly = TRUE)) {
  install.packages("evclass")
}

library(evclass)

ls("package:evclass")

data(iris)
head(iris)

features <- iris[, 1:4]
labels <- iris[, 5]

set.seed(123)

split_data <- function(features, labels, train_ratio = 0.7) {
  n <- nrow(features)
  train_indices <- sample(1:n, size = round(train_ratio * n))
  test_indices <- setdiff(1:n, train_indices)
  
  list(
    train_features = features[train_indices, ],
    train_labels = labels[train_indices],
    test_features = features[test_indices, ],
    test_labels = labels[test_indices]
  )
}

split <- split_data(features, labels)
train_features <- split$train_features
train_labels <- split$train_labels
test_features <- split$test_features
test_labels <- split$test_labels

param0 <- EkNNinit(train_features, train_labels)

options <- list(maxiter = 300, eta = 0.1, gain_min = 1e-5, disp = FALSE)

fit <- EkNNfit(train_features, train_labels, param = param0, K = 5, options = options)

print("Leave-One-Out (LOO) Error Rate for Training Data")
print(fit$err)
print(table(fit$ypred, train_labels))

val <- EkNNval(xtrain = train_features, ytrain = train_labels, xtst = test_features, K = 5, ytst = test_labels, param = fit$param)

print("Error Rate for Test Data")
print(val$err)
print(table(val$ypred, test_labels))
