# Industrial Copper Modeling using Machine Learning


**Key Technologies and Skills**
- Python
- Numpy
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Pickle
- Streamlit


**Features**

**Data Preprocessing:**

- **Data Understanding**: Before diving into modeling, it's crucial to gain a deep understanding of your dataset. Start by identifying the types of variables within it, distinguishing between continuous and categorical variables, and examining their distributions. In our dataset, there might be some unwanted values in the 'Material_Ref' feature that start with '00000.' These values should be converted to null for better data integrity.

- **Handling Null Values**: The dataset may contain missing values that need to be addressed. The choice of handling these null values, whether through mean, median, or mode imputation, depends on the nature of the data and the specific feature.

- **Encoding and Data Type Conversion**: To prepare categorical features for modeling, we employ ordinal encoding. This technique transforms categorical values into numerical representations based on their intrinsic nature and their relationship with the target variable. Additionally, it's essential to convert data types to ensure they match the requirements of our modeling process.

- **Skewness - Feature Scaling**: Skewness is a common challenge in datasets. Identifying skewness in the data is essential, and appropriate data transformations must be applied to mitigate it. One widely-used method is the log transformation, which is particularly effective in addressing high skewness in continuous variables. This transformation helps achieve a more balanced and normally-distributed dataset, which is often a prerequisite for many machine learning algorithms.

- **Outliers Handling**: Outliers can significantly impact model performance. We tackle outliers in our data by using the Interquartile Range (IQR) method. This method involves identifying data points that fall outside the IQR boundaries and then converting them to values that are more in line with the rest of the data. This step aids in producing a more robust and accurate model.

- **Wrong Date Handling**: In cases where some delivery dates are precedes the item dates, we resolve this issue by calculating the difference and it's used to train a Random Forest Regressor model, which enables us to predict the corrected delivery date. This approach ensures that our dataset maintains data integrity and accuracy.


**Exploratory Data Analysis (EDA) and Feature Engineering:**

- **Skewness Visualization**: To enhance data distribution uniformity, we visualize and correct skewness in continuous variables using `Seaborn's Histplot and Violinplot`. By applying the Log Transformation method, we achieve improved balance and normal distribution, while ensuring data integrity.

- **Outlier Visualization**: We identify and rectify outliers by leveraging `Seaborn's Boxplot`. This straightforward visualization aids in pinpointing outlier-rich features. Our chosen remedy is the Interquartile Range (IQR) method, which brings outlier data points into alignment with the rest of the dataset, bolstering its resilience.


**Classification:**

- **Success and Failure Classification**: In our predictive journey, we utilize the 'status' variable, defining 'Won' as Success and 'Lost' as Failure. Data points with status values other than 'Won' and 'Lost' are excluded from our dataset to focus on the core classification task.

- **Handling Data Imbalance**: In our predictive analysis, we encountered data imbalance within the 'status' feature. To address this issue, we implemented the SMOTETomek oversampling method, ensuring our dataset is well-balanced. This enhancement significantly enhances the performance and reliability of our classification tasks, yielding more accurate results in distinguishing between success and failure.

- **Algorithm Assessment**: In the realm of classification, our primary objective is to predict the categorical variable of status. The dataset is thoughtfully divided into training and testing subsets, setting the stage for our classification endeavor. We apply various algorithms to assess their performance and select the most suitable base algorithm for our specific data.

- **Algorithm Selection**: After thorough evaluation, two contenders, the Extra Trees Classifier and Random Forest Classifier, demonstrate commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Random Forest Classifier for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.

- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**: To fine-tune our model and mitigate overfitting, we employ GridSearchCV with cross-validation for hyperparameter tuning. This function allows us to systematically explore multiple parameter values and return the optimal set of parameters. 
			{ 
            'max_depth'      : [5,10,15,20,25,30,40,50,60,70],
            'min_samples_split': [2,3,5,7,8,9,10,15],
            'min_samples_leaf' : [1,2,3,4,5,6,7,8,10],
            'max_features'     : ['sqrt', 'log2', None],
            'n_estimators'      : [5,10,15,25,35,50,100]
            }`			

- **Model Accuracy and Metrics**: With the optimized parameters, our Random Forest Classifier achieves an impressive 98.0% accuracy, ensuring robust predictions for unseen data. To further evaluate our model, we leverage key metrics such as the confusion matrix, precision, recall, F1-score, AUC, and ROC curve, providing a comprehensive view of its performance.

- **Model Persistence**: We conclude this phase by saving our well-trained model to a pickle file. This enables us to effortlessly load the model and make predictions on the status whenever needed, streamlining future applications.


**Regression:**

- **Algorithm Assessment**: In the realm of regression, our primary objective is to predict the continuous variable of selling price. Our journey begins by splitting the dataset into training and testing subsets. We systematically apply various algorithms, evaluating them based on training and testing accuracy using the R2 (R-squared) metric, which signifies the coefficient of determination. This process allows us to identify the most suitable base algorithm tailored to our specific data.

- **Algorithm Selection**: After thorough evaluation, two contenders, the Extra Trees Regressor and Random Forest Regressor, demonstrate commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Random Forest Regressor for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.

- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**: To fine-tune our model and mitigate overfitting, we employ GridSearchCV with cross-validation for hyperparameter tuning. This function allows us to systematically explore multiple parameter values and return the optimal set of parameters.
`			{ 
            'max_depth'      : [5,10,20,50],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf' : [1, 2, 4],
            'max_features'     : ['sqrt', 'log2', None],
            'n_estimators'      : [15,25,35]
            }


- **Model Accuracy and Metrics**: With the optimized parameters, our Random Forest Regressor achieves an impressive 95.6% accuracy. This level of accuracy ensures robust predictions for unseen data. We further evaluate our model using essential metrics such as mean absolute error, mean squared error, root mean squared error, and the coefficient of determination (R-squared). These metrics provide a comprehensive assessment of our model's performance.

- **Model Persistence**: We conclude this phase by saving our well-trained model to a pickle file. This strategic move enables us to effortlessly load the model whenever needed, streamlining the process of making predictions on selling prices in future applications.
