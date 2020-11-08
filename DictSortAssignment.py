assignment_dict = {
	'hello': ['doc1'],
	'my': ['doc1'],
	'name': ['doc1'],
	'is': ['doc1', 'doc2'],
	'james': ['doc1', 'doc2'],
	'a': ['doc2'],
	'developer': ['doc2']
} 
    
def sortDict(input):
  result= []
  for key in sorted(input): 
    result.append((key, sorted(input[key])))
  
  return result

print(sortDict(assignment_dict))  
