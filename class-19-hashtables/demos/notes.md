## In Class Pseudo Code
```
class Hashtable:
    _array = [None] * 1024
    Hash(key):
        # get the ascii code of each character in key and sum them
        sum = ….
        Multiple_of_prime = sum * 599
        Safe_index = Multiple_of_prime // Len(_array
        Return Safe_Index
    Add(key, value):
        Index = Hash(key)
        # If no bucket at that index then create one and insert it there

        _array[Index].insert((key, value,)). # [(foo,bar)] -> [(oof,baz)] ->
        
    Get(key):
        Index = Hash(key)
        
        # traverse linked list until value[0] == key then return value[1] 
        # handle unknown key

Ht = HashTable()
HT.Add(‘foo’,’bar’)
HT.Get(‘foo’)
HT.Add(‘oof’,’baz’)
```
