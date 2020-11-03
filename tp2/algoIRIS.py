import seaborn as sns
import sklearn
import joblib 
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split

def accuracy(preds, Y):
    return (preds == Y).sum() / len(Y) * 100

iris = sns.load_dataset('iris')

Y = iris['species'].astype('category').cat.codes
X = iris.drop('species', axis='columns')

#stratify permet de prendre un échantillon représentatif de valeur pour le train
#random_state permet de prendre les données de manière random
#train_size permet de définir la taille du nombre de données pris pour l'entrainement 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.3, stratify=Y,random_state=2)

knn = KNN(n_neighbors=3)
knn.fit(X_train,Y_train)

Y_pred = knn.predict(X_test)
print(accuracy(Y_pred,Y_test))

joblib.dump(knn, 'modelIRIS.pkl')




