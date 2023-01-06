
# Bank Note Authentication

The aim is to detect fraudulent notes acurately.
Features such as variance, skewness, curtosis and entropy are taken in account.

Its a binary classification application, determining whether the output is 0 or 1 (fraudulent or legal)



## Requirement
- Python 3.7.3

Required libraries:

- numpy 1.16.2
- pandas 0.24.2
- sklearn 0.20.3
- seaborn 0.9.0
- matplotlib 3.0.3
- Flask 1.1.2
- Flasgger 0.9.5
## Dataset
The dataset file BankNote_Authentication.csv is the source of information for this project.
There are total 5 columns with 4 independent features namely variance, skewness, curtosis and entropy.
There are total 1372 records(rows) in the dataset.
## Test Analysis
The aim of testing is to velidate the performance of the trained model
ROC curve is a good way to measure for precision of this binary classification model

![AUC_ROC](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/auc_roc.PNG)

The area under curve of the model is 0.991 (approx~1), which means that the model predicts well.

In the confusion matrix, the rows represent the target classes and the columns the output classes for the testing target data set. 
The diagonal cells in each table show the number of correctly classified cases, and the off-diagonal cells show the misclassified instances. 

![confusion_matrix](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/confusion_matrix.PNG)

The following table contains the elements of the confusion matrix.

|               | Predicted Positive     | Predicted Negative |
| :------------ | :------- | :------------------------------- |
| True Positive | 178      | 2                                |
| True Negative | 3        | 229                              |

- True Positive(TP) signifies how many positive class samples your model predicted correctly.
- True Negative(TN) signifies how many negative class samples your model predicted correctly.
- False Positive(FP) signifies how many negative class samples your model predicted incorrectly. This factor represents Type-I error in statistical nomenclature. This error positioning in the confusion matrix depends on the choice of the null hypothesis.
- False Negative(FN) signifies how many positive class samples your model predicted incorrectly. This factor represents Type-II error in statistical nomenclature. This error positioning in the confusion matrix also depends on the choice of the null hypothesis.

Precision, Recall and F1 score are the performance matrix used to evaluate classification model

- Precision is the ratio of true positives and total positives predicted.
- Recall is essentially the ratio of true positives to all the positives in ground truth.
- The F1-score metric uses a combination of precision and recall. In fact, the F1 score is the harmonic mean of the precision and recall.

![performance_matrix](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/performance_matrx.PNG)


## Screenshots of Swagger API
Swagger helps users build, document, test and consume RESTful web services. It can be used with both a top-down and bottom-up API development approach.

![Swagger API](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/swagger1.PNG)

![Swagger API](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/swagger2.PNG)

![Swagger API](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/swagger3.PNG)



## Postman
Postman is an API platform for building and using APIs

![postman](https://github.com/DragnaRR/Bank-note-authentication/blob/main/bank%20note%20authentication/screenshot/postman.PNG)
