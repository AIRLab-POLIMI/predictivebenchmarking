
import pickle

import numpy as np 
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern as MA, RationalQuadratic as RQ ,DotProduct as DP, ExpSineSquared as ESS, ConstantKernel as C
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

datafile = open('pickle.p')
data = pickle.load(datafile)

fields = ['dataset', ' Voronoi distance', ' Voronoi rotation', ' totalLen', ' totalRot', ' transError.mean.mean', ' transError.mean.std', ' rotError.mean.mean', ' rotError.mean.std']

features = [' Voronoi distance', ' Voronoi rotation']
targets = [' transError.mean.mean', ' transError.mean.std', ' rotError.mean.mean', ' rotError.mean.std']

X = []
Y0 = []
Y1 = []
Y2 = []
Y3 = []
Y0_BEST = -100
Y0_PARAM = None
Y1_BEST = -100
Y1_PARAM = None
Y2_BEST = -100
Y2_PARAM = None
Y3_BEST = -100
Y3_PARAM = None
keys = []
for i in data.keys() :
	if i != 'columns' :
		tmp_x = [data[i][j] for j in features]
		X.append(tmp_x)
		Y0.append(data[i][targets[0]])
		Y1.append(data[i][targets[1]])
		Y2.append(data[i][targets[2]])
		Y3.append(data[i][targets[3]])

# finishing pasing data, now start testing 

# Instanciate a Gaussian Process model
#kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
#gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
# TESTIND DIFFERENT KERNELS
printMSE = True 
printDetails = False 
kernels = [RBF(),MA(),RQ(),RQ(length_scale=50)]
for kernel in kernels :
	print kernel
	gp = GaussianProcessRegressor(kernel) #n_restarts_optimizer)

	clf = gp

	print "variable number 1: " + targets[0]
	scores = cross_val_score(clf, X, Y0, cv=5,scoring='r2')
	if printDetails :
		print scores 
	print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
	if printMSE :
		scores = cross_val_score(clf, X, Y0, cv=5,scoring='neg_mean_squared_error')
		if printDetails :
			print scores 
		print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
		print "RMSE = " + str(np.sqrt(-scores.mean()))

	print "variable number 2: " + targets[1]
	scores = cross_val_score(clf, X, Y1, cv=5,scoring='r2')
	if printDetails :
		print scores 
	print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
	if printMSE :
		scores = cross_val_score(clf, X, Y1, cv=5,scoring='neg_mean_squared_error')
		if printDetails :
			print scores 
		print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
		print "RMSE = " + str(np.sqrt(-scores.mean()))

	print "variable number 3: " + targets[2]
	scores = cross_val_score(clf, X, Y2, cv=5,scoring='r2')
	if printDetails :
		print scores 
	print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
	if printMSE :
		scores = cross_val_score(clf, X, Y2, cv=5,scoring='neg_mean_squared_error')
		if printDetails :
			print scores 
		print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
		print "RMSE = " + str(np.sqrt(-scores.mean()))

	print "variable number 4: " + targets[3]
	scores = cross_val_score(clf, X, Y3, cv=5,scoring='r2')
	if printDetails :
		print scores 
	print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
	if printMSE :
		scores = cross_val_score(clf, X, Y3, cv=5,scoring='neg_mean_squared_error')
		if printDetails :
			print scores 
		print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
		print "RMSE = " + str(np.sqrt(-scores.mean()))

	print '\n'*3


# BEST RMSE 
# RBF
# trying different kernel parameters select those with BEST RMSE
print "START COMPUTING"
opti = 0
for length_scale in [1+k*5 for k in range(10)] :
	for alpha in [1e-10*10**p for p in range(10)] :
		print length_scale
		gp = GaussianProcessRegressor(RBF(length_scale),alpha, n_restarts_optimizer=opti)
		scores = cross_val_score(gp, X, Y0, cv=5,scoring='neg_mean_squared_error')
		if scores.mean() > Y0_BEST :
			Y0_BEST = scores.mean()
			Y0_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y1, cv=5,scoring='neg_mean_squared_error')
		if scores.mean() > Y1_BEST :
			Y1_BEST = scores.mean()
			Y1_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y2, cv=5,scoring='neg_mean_squared_error')
		if scores.mean() > Y2_BEST :
			Y2_BEST = scores.mean()
			Y2_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y3, cv=5,scoring='neg_mean_squared_error')
		if scores.mean() > Y3_BEST :
			Y3_BEST = scores.mean()
			Y3_PARAM = (length_scale,alpha)

print Y0_BEST, Y0_PARAM
gp = GaussianProcessRegressor(RBF(Y0_PARAM[0]),Y0_PARAM[1],n_restarts_optimizer=opti) #n_restarts_optimizer)
print "variable number 1: " + targets[0]
scores = cross_val_score(gp, X, Y0, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y0, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
print '\n'*3

print Y1_BEST, Y1_PARAM
gp = GaussianProcessRegressor(RBF(Y1_PARAM[0]),Y1_PARAM[1],n_restarts_optimizer=opti) #n_restarts_optimizer)
print "variable number 2: " + targets[1]
scores = cross_val_score(gp, X, Y1, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y1, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
print '\n'*3

print Y2_BEST, Y2_PARAM
gp = GaussianProcessRegressor(RBF(Y2_PARAM[0]),Y2_PARAM[1],n_restarts_optimizer=opti) #n_restarts_optimizer)
print "variable number 3: " + targets[2]
scores = cross_val_score(gp, X, Y2, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y2, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
print '\n'*3

print Y3_BEST, Y3_PARAM
gp = GaussianProcessRegressor(RBF(Y3_PARAM[0]),Y3_PARAM[1]) #n_restarts_optimizer)
print "variable number 4: " + targets[3]
scores = cross_val_score(gp, X, Y3, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y3, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))



exit()
# RBF
# trying  different kernel parameters select those with BEST R2
print "START COMPUTING"
for length_scale in [1+k*5 for k in range(10)] :
	for alpha in [1e-10*10**p for p in range(10)] :
		print length_scale
		gp = GaussianProcessRegressor(RBF(length_scale),alpha)
		scores = cross_val_score(gp, X, Y0, cv=5,scoring='r2')
		if scores.mean() > Y0_BEST :
			Y0_BEST = scores.mean()
			Y0_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y1, cv=5,scoring='r2')
		if scores.mean() > Y1_BEST :
			Y1_BEST = scores.mean()
			Y1_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y2, cv=5,scoring='r2')
		if scores.mean() > Y2_BEST :
			Y2_BEST = scores.mean()
			Y2_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y3, cv=5,scoring='r2')
		if scores.mean() > Y3_BEST :
			Y3_BEST = scores.mean()
			Y3_PARAM = (length_scale,alpha)

print Y0_BEST, Y0_PARAM
gp = GaussianProcessRegressor(RBF(Y0_PARAM[0]),Y0_PARAM[1]) #n_restarts_optimizer)
print "variable number 1: " + targets[0]
scores = cross_val_score(gp, X, Y0, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y0, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
print '\n'*3

print Y1_BEST, Y1_PARAM
gp = GaussianProcessRegressor(RBF(Y1_PARAM[0]),Y1_PARAM[1]) #n_restarts_optimizer)
print "variable number 2: " + targets[1]
scores = cross_val_score(gp, X, Y1, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y1, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
print '\n'*3

print Y2_BEST, Y2_PARAM
gp = GaussianProcessRegressor(RBF(Y2_PARAM[0]),Y2_PARAM[1]) #n_restarts_optimizer)
print "variable number 3: " + targets[2]
scores = cross_val_score(gp, X, Y2, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y2, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
print '\n'*3

print Y3_BEST, Y3_PARAM
gp = GaussianProcessRegressor(RBF(Y3_PARAM[0]),Y3_PARAM[1]) #n_restarts_optimizer)
print "variable number 4: " + targets[3]
scores = cross_val_score(gp, X, Y3, cv=5,scoring='r2')
print "R2: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
scores = cross_val_score(gp, X, Y3, cv=5,scoring='neg_mean_squared_error')
print "MSE: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
print "RMSE = " + str(np.sqrt(-scores.mean()))
exit()

# TEST FOR RQ KERNEL 
print "START COMPUTING"
for length_scale in [0.2+k*0.5 for k in range(10)] :
	for alpha in [0.2+p*0.5 for p in range(10)] :
		print length_scale, alpha 
		gp = GaussianProcessRegressor(RQ(length_scale,alpha))
		scores = cross_val_score(gp, X, Y0, cv=5,scoring='r2')
		if scores.mean() > Y0_BEST :
			Y0_BEST = scores.mean()
			Y0_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y1, cv=5,scoring='r2')
		if scores.mean() > Y1_BEST :
			Y1_BEST = scores.mean()
			Y1_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y2, cv=5,scoring='r2')
		if scores.mean() > Y2_BEST :
			Y2_BEST = scores.mean()
			Y2_PARAM = (length_scale,alpha)
		scores = cross_val_score(gp, X, Y3, cv=5,scoring='r2')
		if scores.mean() > Y3_BEST :
			Y3_BEST = scores.mean()
			Y3_PARAM = (length_scale,alpha)

print Y0_BEST
print Y1_BEST
print Y2_BEST
print Y3_BEST
