import numpy as np
from matplotlib import pyplot as plt
# BASIS_PATH= "basis_data1_2500/basis_array_"

def wrapping_controlps(basis_path):
	# points4 = np.array([[1,1],[1,1],[1,1],[1,1]])
	# points5 = np.array([[1,1],[3,4],[1,1],[3,4],[1,1]])
	points7 = np.array([[1,1],[2,3],[3,2],[3,1],[1,1], [2, 3], [3,2]])
	points11 = np.array([[1,1],[2,3],[3,2],[3,1],[4,0],[5,0],[6,-2],[4,-5],[1,1],[2,3],[3,2]])

	n = 2 ** 3 + 3 - 1
	m = n+3+1

	points = points11
	points_x = points[:,0]
	points_y = points[:,1]
	points_x_mat = np.mat(points_x)
	points_y_mat = np.mat(points_y)

	# plt.plot(np.concatenate((points_x, np.array([points_x[0]]))), np.concatenate((points_y, np.array([points_y[0]]))), '--')
	plt.plot(points_x, points_y, '--')


	phi_j_1 = np.loadtxt(basis_path + str(n+1) + ".txt")
	# m_phi=np.mat(phi_j)
	m_phi_1 = np.mat(phi_j_1)
	x_spline_1 = points_x_mat * m_phi_1.T
	y_spline_1 = points_y_mat * m_phi_1.T

	plt.plot(np.array(x_spline_1).flatten(), np.array(y_spline_1).flatten())

	x_spline_1_array = np.array(x_spline_1).flatten()
	y_spline_1_array = np.array(y_spline_1).flatten()
	# x_spline_1_array = x_spline_1_array[int(3/m*len(x_spline_1_array)):-int(3/m*len(x_spline_1_array))]
	# y_spline_1_array = y_spline_1_array[int(3/m*len(y_spline_1_array)):-int(3/m*len(y_spline_1_array))]
	plt.plot(x_spline_1_array, y_spline_1_array)

	# new_list_x = np.concatenate((x_spline_1_array[-600:], x_spline_1_array[:600]), axis=0)
	# new_list_y = np.concatenate((y_spline_1_array[-600:], y_spline_1_array[:600]), axis=0)
	#
	# plt.plot(new_list_x, new_list_y)

	for i in range(len(x_spline_1_array)):
		if i%400==0:
			plt.text(x_spline_1_array[i], y_spline_1_array[i], str(i))

	# plt.show()
	plt.savefig("output/wrapping_controlps.png")

def wrapping_knots(basis_path):
	points7 = np.array([[1,1],[2,3],[3,4],[4,6],[5,5],[4,2],[3, -2], [1,1]])
	points11 = np.array([[1,1],[2,3],[3,2],[3,1],[4,0],[5,0],[6,-2],[5,-4],[4,-7],[3,-6],[2,-3], [1,1]])

	n = 2 ** 3 + 3 - 1
	k = 3
	m = n+k+1

	points = points11
	points_x = points[:,0]
	points_y = points[:,1]
	points_x_mat = np.mat(points_x)
	points_y_mat = np.mat(points_y)

	# plt.plot(np.concatenate((points_x, np.array([points_x[0]]))), np.concatenate((points_y, np.array([points_y[0]]))), '--')
	plt.plot(points_x, points_y, '--')


	phi_j_1 = np.loadtxt(basis_path + str(n+1) + ".txt")
	# m_phi=np.mat(phi_j)
	m_phi_1 = np.mat(phi_j_1)
	x_spline_1 = points_x_mat * m_phi_1.T
	y_spline_1 = points_y_mat * m_phi_1.T

	plt.plot(np.array(x_spline_1).flatten(), np.array(y_spline_1).flatten())

	x_spline_1_array = np.array(x_spline_1).flatten()
	y_spline_1_array = np.array(y_spline_1).flatten()
	# x_spline_1_array = x_spline_1_array[int(3/m*len(x_spline_1_array)):-int(3/m*len(x_spline_1_array))]
	# y_spline_1_array = y_spline_1_array[int(3/m*len(y_spline_1_array)):-int(3/m*len(y_spline_1_array))]
	plt.plot(x_spline_1_array, y_spline_1_array)

	# new_list_x = np.concatenate((x_spline_1_array[-600:], x_spline_1_array[:600]), axis=0)
	# new_list_y = np.concatenate((y_spline_1_array[-600:], y_spline_1_array[:600]), axis=0)
	#
	# plt.plot(new_list_x, new_list_y)

	for i in range(len(x_spline_1_array)):
		if i%400==0:
			plt.text(x_spline_1_array[i], y_spline_1_array[i], str(i))

	# plt.show()
	plt.savefig("output/wrapping_knots.png")

def test():
	points = np.array([[1,1], [3,2], [4,1], [1,1]])
	u_raw=[[0,1/5], [1/5, 2/5], [2/5, 3/5], [3/5, 4/5], [4/5,1], [1,0]]
	x=[lambda u: 25/2*u**2, lambda u: 25/2*u**2, lambda u: -25/2*u**2+20*u-4, lambda u: -50*u**2+65*u-35/2, lambda u: 175/4*u**2-85*u+85/2,
	   lambda u: 5/4*u**2]
	y=[lambda u: 25/2*u**2, lambda u: 5*u-1/2, lambda u: -25*u**2+25*u-9/2, lambda u: 25/2*u**2-20*u+9, lambda u: 25/4*u**2-10*u+5,
	   lambda u: 5/4*u**2]
	x_list = []
	y_list = []
	for i in range(len(u_raw)):
		l, r = u_raw[i][0], u_raw[i][1]
		step = 0.004
		if l>r:
			step = -step
		u = np.arange(l, r, step)

		for u_ in u:
			x_part = x[i](u_)
			y_part = y[i](u_)
			x_list.append(x_part)
			y_list.append(y_part)
	plt.plot(x_list, y_list)

	plt.plot(points[:,0], points[:,1], "*")
	plt.show()

# wrapping_controlps("basis_data1_2500/basis_array_")
wrapping_knots("basis_data2_2500/basis_array_")
# test()