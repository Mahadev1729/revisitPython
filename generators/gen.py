# def get_square(n):
#     result=[]
#     for i in range(n):
#         result.append(i*i)
#     return result

    
# ans=[]
# ans=get_square(5)
# print(ans)

def get_square_gen(n):
    for i in range(n):
        yield i*i
       
for i in get_square_gen(5):
    print(i)       
