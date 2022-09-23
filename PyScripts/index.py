import os

print('-'*30)
loc = "./docs"
file_list = os.listdir(loc)
print(loc, '의 문서 수는:', len(file_list))
print('-'*30)

ix= ['- [['+name[:-3]+']]\n' for name in file_list]

print(ix)
    
    
with open('./result.txt', 'w') as file:
    file.writelines(ix)
file.close()