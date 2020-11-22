# https://leetcode.com/problems/reverse-words-in-a-string-ii/
#186. Reverse Words in a String II
#
#    Question
#    Solution
#
#
#Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
#
#The input string does not contain leading or trailing spaces and the words are always separated by a single space.
#
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".
#
#Could you do it in-place without allocating extra space? 

public void reverseWords(char[] s) {
    int i=0;
    for(int j=0; j<s.length; j++){
        if(s[j]==' '){
            reverse(s, i, j-1);        
            i=j+1;
        }
    }
 
    reverse(s, i, s.length-1);
 
    reverse(s, 0, s.length-1);
}
 
public void reverse(char[] s, int i, int j){
    while(i<j){
        char temp = s[i];
        s[i]=s[j];
        s[j]=temp;
        i++;
        j--;
    }
}

# Function to reverse words of string 
  
def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ')  
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words))  
  
    # finally return the joined string 
    return reverse_sentence   
  
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print rev_sentence(input) 


class Solution:
    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        str_list = ''.join(str).split(' ')
        str_list.reverse()
        ans = ' '.join(str_list)
        str[:] = list(ans)
