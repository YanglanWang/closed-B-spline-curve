import scipy.signal as ss
import numpy as np
import scipy.misc as mi
import matplotlib.pyplot as plt


def deboor(k, t):
	m = len(t) - 1
	a, b, _k, _m = [], [], range(k + 1), range(m)
	for i in _m:
		a.append([])
		b.append([])
		for k in _k:
			a[i].append(None)
			if (k == 0):
				b[i].append(lambda t_, i=i: t[i] <= t_ < t[i + 1])
			elif m < i + k:
				b[i].append(lambda t_: False)
			else:
				if t[i] == t[i + k]:
					a[i][k] = lambda t_: False
				else:
					a[i][k] = lambda t_, i=i, k=k: ((t_ - t[i]) / (t[i + k] - t[i]))
				b[i].append(
					lambda t_, i=i, k=k: a[i][k](t_) * b[i][k - 1](t_) + (1 - a[i + 1][k](t_)) * b[i + 1][k - 1](t_))
	return b  # set b


for power in range(11):
	n = 2 ** power + 3 - 1
	print("Generating Basis with " + str(n + 1) + " elements")
	k = 3  # degree of curve
	m = n + k + 1  # property of b-splines: m = n + k + 1
	# [Uk, Um-k) 1/(m-2k)
	# _t = 1.0 / m  # t between clamped ends will be evenly spaced (not a necessary condition, however)
	# t = [t_ * _t for t_ in range(m + 1)]

	_t = 1.0 / (m - k * 2)  # t between clamped ends will be evenly spaced (not a necessary condition, however)
	t = [t_*_t for t_ in range(-k, 0, 1)] + [t_ * _t for t_ in range(m - (k * 2) + 1)] + [1+t_*_t for t_ in range(1, k+1)]

	b = deboor(k, t)
	# _n=range(len(t)-1-k-1+1)
	t_ = np.arange(t[3], t[-4], .0004)

	f_h = open("./basis_data1_2500/basis_array_" + str(n + 1) + ".txt", 'w')
	u_len = len(t_)
	at_first = 1
	for i in t_:
		dummy = np.array([])
		for j in range(n + 1):
			# for j in range(n+1+4):
			dummy = np.append(dummy, b[j][k](i))
		if at_first == 1:
			at_first = 0
			b_mat = dummy
		else:
			b_mat = np.vstack((b_mat, dummy))
	np.savetxt(f_h, b_mat)
	f_h.close()
	print("save basic with {} elements".format(n + 1))

	for i in range(n + 1):
		plt.plot(t_, b_mat[:, i])
	plt.savefig("./basis_data1_2500/basis_fig_" + str(n + 1) + ".png")
	plt.clf()
	print("Generation and Saving figure complete")
	# plt.show()