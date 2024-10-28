input_line=input().split()
N=int(input())
result_list=[]
for i in input_line:
    word=i
    if len(word)!=N:
        result_list.append(word)
result_list=" ".join(result_list)
print(result_list)
