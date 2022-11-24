from sklearn import tree

# Database: Gerbang logika AND
# X = Data, Y = Target
x = [[0,0], [0,1], [1,0], [1,1], [0,2], [1,2], [2,2], [2,0], [2,1], [2,3]]
y = [0,0,0,1,0,2,4,0,2,6]

# Training and Classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Decision Tree")
print("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("0 2 = ", clf.predict([[0,2]]))
print ("1 2 = ", clf.predict([[1,2]]))
print ("2 2 = ", clf.predict([[2,2]]))
print ("2 0 = ", clf.predict([[2,0]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("2 3 = ", clf.predict([[2,3]]))
