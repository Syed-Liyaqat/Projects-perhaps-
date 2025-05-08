from sklearn.linear_model import LinearRegression
#x-independent values
x=[[1],[2],[3],[4],[5]]
#y-dependent values, y=7x+9 (y=mx=b)
y=[[16],[23],[30],[37],[44]]
model=LinearRegression()
#this will guess the pattern based on data given
model.fit(x,y)
#lets check what the model predicted the patter/linear expression to be
coeff = model.coef_[0][0] #also called as slope
const = model.intercept_[0] #also called as intercept 
va = int(input("Enter the value you want to predict the data for: ")) #va= value at
prediction = model.predict([[va]])
print(f"The model predicted pattern to be: y = {coeff:.2f}x+{const:.2f}")
print(f"next value is predicted to be - {prediction}")