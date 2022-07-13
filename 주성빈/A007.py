num_list = list(map(int, input().split()))

if(all(num_list[i] < num_list[i+1] for i in range(len(num_list)-1))):
  print("ascending")
elif(all(num_list[i]>num_list[i+1] for i in range(len(num_list)-1))):
  print("descending")
else:
  print("mixed")
