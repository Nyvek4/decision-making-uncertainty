if (!requireNamespace("evclass", quietly = TRUE)) {
  install.packages("evclass", lib = Sys.getenv("R_LIBS_USER"))
}

library(evclass)
library(jsonlite)  # Ajout de la bibliothèque jsonlite pour l'exportation au format JSON

# Retrieve the argument from the command line
args <- commandArgs(trailingOnly = TRUE)
if (length(args) == 0) {
  stop("No argument provided. Please provide a string argument.")
}
output_prefix <- args[1]

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

# Split the original data
split <- split_data(features, labels)
train_features <- split$train_features
train_labels <- split$train_labels
test_features <- split$test_features
test_labels <- split$test_labels

# Simulate a second source of information by adding noise to the features
set.seed(456)
noise <- matrix(rnorm(nrow(features) * ncol(features), mean = 0, sd = 0.1), nrow = nrow(features))
features_IS2 <- features + noise

# Split the second source data
split_IS2 <- split_data(features_IS2, labels)
train_features_IS2 <- split_IS2$train_features
train_labels_IS2 <- split_IS2$train_labels
test_features_IS2 <- split_IS2$test_features
test_labels_IS2 <- split_IS2$test_labels

# Train the model on the first dataset
param0 <- EkNNinit(train_features, train_labels)
options <- list(maxiter = 300, eta = 0.1, gain_min = 1e-5, disp = FALSE)
fit <- EkNNfit(train_features, train_labels, param = param0, K = 5, options = options)

print("Leave-One-Out (LOO) Error Rate for Training Data (IS1)")
print(fit$err)
print(table(fit$ypred, train_labels))

val <- EkNNval(xtrain = train_features, ytrain = train_labels, xtst = test_features, K = 5, ytst = test_labels, param = fit$param)

print("Error Rate for Test Data (IS1)")
print(val$err)
print(table(val$ypred, test_labels))

# Export the BBAS file for the first dataset in JSON format
if (!file.exists("datasets\\"+output_prefix)) {
  dir.create("datasets\\"+output_prefix)
}
write_json(fit$param, path = paste0("datasets/", output_prefix,"/",output_prefix+"_IS1.json"))

# Train the model on the second dataset
param0_IS2 <- EkNNinit(train_features_IS2, train_labels_IS2)
fit_IS2 <- EkNNfit(train_features_IS2, train_labels_IS2, param = param0_IS2, K = 5, options = options)

print("Leave-One-Out (LOO) Error Rate for Training Data (IS2)")
print(fit_IS2$err)
print(table(fit_IS2$ypred, train_labels_IS2))

val_IS2 <- EkNNval(xtrain = train_features_IS2, ytrain = train_labels_IS2, xtst = test_features_IS2, K = 5, ytst = test_labels_IS2, param = fit_IS2$param)

print("Error Rate for Test Data (IS2)")
print(val_IS2$err)
print(table(val_IS2$ypred, test_labels_IS2))

# Export the BBAS file for the second dataset in JSON format
write_json(fit_IS2$param, path = paste0("datasets/", output_prefix,"/",output_prefix+"_IS2.json"))