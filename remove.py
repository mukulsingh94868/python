num1 = input("enter the string:")
num2 = input("what you want to remove:")



def removeChar(s, c) : 
      
   
    counts = s.count(c) 
  
    
    s = list(s) 
  
   
    while counts : 
          
        
        s.remove(c) 
  
        
        counts -= 1
  
    s = '' . join(s) 
      
    print(s) 

if __name__ == '__main__' : 
      
    s = num1
    removeChar(s,num2) 
