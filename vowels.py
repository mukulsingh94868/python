def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
    print(final) 
      
# Driver Code 
string = "mukul singh is super hero"
vowels = "AeEeIiOoUu"
Check_Vow(string, vowels); 

    
