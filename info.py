import os
for k, v in os.environ.items():
	print('{:33} {}'.format(k, v))