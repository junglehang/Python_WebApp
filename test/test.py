from functools import reduce


def statistics(dic,k):
  if not k in dic:
    dic[k] = 1
  else:
    dic[k] +=1
  return dic
lst = [1,1,2,3,2,3,3,5,6,7,7,6,5,5,5]
print (reduce(statistics,lst,{}) )
#提供第三个参数，第一次，初始字典为空，作为statistics的第一个参数，然后遍历lst,作为第二个参数，然后将返回的字典集合作为下一次的第一个参数
d = []
d.append({})
d.extend(lst) 
print(reduce(statistics,d) )
#不提供第三个参数，但是要在保证集合的第一个元素是一个字典对象，作为statistics的第一个参数，遍历集合依次作为第二个参数