import numpy as np
print("="*40)
print("Creating 3 arrays")
print("="*40)

print("\n 1st array")
a1=np.array([[1,2,3,4,56,23,12,45,67,23]])
print(f"\n" ,a1)
print("\n SHAPE: ",a1.shape)

print("\n 2nd array")
a2=np.array([[[4,56,76],[75,348,93]]])
print("\n",a2)
print("\n SHAPE: ",a2.shape)

print("\n 3rd array")
a3=np.array([[[35,67],[4,56],[75,348]]])
print("\n",a3)
print("\n SHAPE: " , a3.shape)

print("="*40)
print("Reshaping arrays")
print("="*40)

a2_r=a2.reshape(1 ,3 ,2)
print("\n a2 reshaped to (1,3,2):\n",a2_r)
print("\n Shape: ",a2_r.shape)

a1_r=a1.reshape(1,2,5)
print("\n a1 reshaped to (1,2,5):\n",a1_r)
print("\n Shape: ",a1_r.shape)

