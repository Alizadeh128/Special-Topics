##تمرین چهارم : با استفاده از Logistic regression بر روی مجموع داده Iris flower data set یک مسئله دو کلاسه تعریف کرده و accuracy مدل خود را بدست آورید

# بارگیری کتابخانه‌های مورد نیاز
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# بارگیری مجموعه داده Iris
iris = load_iris()
X = iris.data
y = iris.target

# انتخاب فقط داده‌های مربوط به دو کلاس اولیه (Iris-setosa و Iris-versicolor)
X = X[y != 2]
y = y[y != 2]

# تقسیم داده‌ها به داده‌های آموزش و آزمون
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل Logistic Regression و آموزش آن روی داده‌های آموزش
model = LogisticRegression()
model.fit(X_train, y_train)

# پیش‌بینی کلاس‌های داده‌های آزمون
y_pred = model.predict(X_test)

# محاسبه دقت مدل
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
