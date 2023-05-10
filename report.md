Hi Xenia,

There have been numerous research papers published on this topic, using different machine learning algorithms and techniques. However, the accuracy of the classification depends on the quality of the features extracted from the packet captures and the effectiveness of the machine learning algorithm used.

For example, the following research papers are a good starting point:

 1. "IoT Malicious Traffic Classification Using Machine Learning" (2019), which uses six different machine learning algorithms to identify IoT traffic: Naive Bayes, Decision Tree, Random Forest, K-Nearest Neighbor (KNN), Support Vector Machine (SVM) and Logistic Regression. 

 2. "Deep Learning for Network Traffic Monitoring and Analysis" (2021), which uses different deep learning models to classify network traffic :autoencoders, stacked autoencoders, convolutional neural networks (CNN), and long short-term memory (LSTM).

3. "A Machine Learning Approach for Reconnaissance Detection to Improve Intrusion Detection System" (2022), which uses a hybrid intrusion detection model that is based on the enhanced genetic algorithm and particle swarm optimization (EGA-PSO) algorithm to detect reconnaissance attacks. The study does not seem to involve using multiple machine learning models

If the car does not start, one would check the battery.If the tire pressure is low, the first thing to do is physically observe it and detect the problem.Following this logic, it is recommended to start with a simple model and gradually increase the complexity until the best performance is reached.

Since we are starting with a simple model, the best option would be to begin with using Decision Trees or Random Forests (tend to perform better).

After using Random Forests for malware classification, the next step would be to evaluate the performance of the model on a validation set or using cross-validation techniques. We can use metrics such as accuracy, precision, recall, and F1-score to evaluate the performance of the model.

If the performance is not satisfactory, you can try tuning the hyperparameters of the Random Forest model to improve performance. One approach is to use grid search or random search to find the best combination of hyperparameters such as the number of estimators, the depth of the trees, and the number of features to consider at each split.

If the performance is still not satisfactory, you can try using more complex models such as SVMs or CNNs, which may be able to capture more complex patterns in the data. However,  these models may require more computational resources and training time.

In any case, it is important to properly validate and evaluate the performance of the models to ensure that they are effective at detecting malware.

