# Source node: 1, 2

# Trans shipment node: 2, 3, 4, 5

# Destination node: 6

# Minimize 2 t12 + 3 t13 + 3 t15 + 2 t23 + 4 t24 + 1 t34 + 2 t35 + 3 t46 + 1 t56

# t12 + t13 + t15 = 1 (node 1)

# t12 - t24 - t23 = -3 (node 2)

# t13 + t23 - t34 - t35 = 0 (node 3)

# t24 + t34 - t46 = 0 (node 4)

# t15 + t35 - t56 = 0 (node 5)

# t46 + t56 = 4 (node 6)

# tij >= 0



# Transportation table (shows distance matrix):

# From \ To	2	3	4	5	Capacity
# 1	2	3	99	3	1
# 2	0	2	4	99	3
# From \ To	2	3	4	5	6
# 2	0	2	4	99	99
# 3	99	0	1	2	99
# 4	99	99	0	99	3
# 5	99	99	99	0	1
# Demand	0	0	0	0	4
# Solution

# From \ To	2	3	4	5	Sent
# 1	0	0	0	1	1
# 2	0	3	0	0	3
# 0	3	0	1	
# From \ To	2	3	4	5	6
# 2	0	0	0	0	0
# 3	0	0	0	3	0
# 4	0	0	0	0	0
# 5	0	0	0	0	4
# Received	0	0	0	3	4