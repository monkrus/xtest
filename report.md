**Research challenge** : Use pcapng files to classify malware.

**Initial setup**: Unzip pcapng and pcap files for simplicity.

**Chain of thought** : 
- read and parse both benign and malicious data
- **pretest data readings**
- combine the malicious and benign data into a single dataset
- label the data with 1 for malicious and 0 for benign
- divide the dataset into training and testing sets
- use a machine learning algorithm to train a model on the training set. Make sure to tune the hyperparameters of the classifier.
- test the accuracy of the model on the testing set. Use metrics like confusion matrix, precision, recall, F1 score, and accuracy to evaluate the performance of the model.

**Model**: *Will start with a simple model and gradually increase the complexity until the best performance is reached.*
One of the good options will be Random Forests, as it searches for the best feature among a random subset of features.

**Next steps**
After using Random Forests for malware classification, the next step would be to evaluate the performance of the model on a validation set or using cross-validation techniques. We can use metrics such as accuracy, precision, recall, and F1-score to evaluate the performance of the model.

If the performance is not satisfactory, one can try tuning the hyperparameters of the Random Forest model to improve performance. One approach is to use grid search or random search to find the best combination of hyperparameters such as the number of estimators, the depth of the trees, and the number of features to consider at each split.

If the performance is still not satisfactory, we should try using more complex models such as SVMs or CNNs, which may be able to capture more complex patterns in the data. However, these models may require more computational resources and training time.

**Reference to publications**:
 1. "IoT Malicious Traffic Classification Using Machine Learning" (2019). Uses six different machine learning algorithms to identify IoT traffic: Naive Bayes, Decision Tree, *Random Forest*, K-Nearest Neighbor (KNN), Support Vector Machine (SVM) and Logistic Regression. 
 
 2. "Deep Learning for Network Traffic Monitoring and Analysis" (2021), they use different deep learning models to classify network traffic :autoencoders, stacked autoencoders, convolutional neural networks (CNN), and long short-term memory (LSTM).
 
 3. "A Machine Learning Approach for Reconnaissance Detection to Improve Intrusion Detection System" (2022), utilize a hybrid intrusion detection model that is based on the enhanced genetic algorithm and particle swarm optimization (EGA-PSO) algorithm to detect reconnaissance attacks. The study does not seem to involve using multiple machine learning models




