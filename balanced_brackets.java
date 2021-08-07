class Result {

    /*
     * Complete the 'isBalanced' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String isBalanced(String str) {
    // Write your code here
    // Storing delimiters for easy reference
        HashMap<Character, Character> delimiters = new HashMap<Character, Character>();
        delimiters.put('(', ')');
        delimiters.put('[', ']');
        delimiters.put('{', '}');
      
        // Stack to track delimiters and check if they are matching
        Stack<Character> stack = new Stack<Character>();
      
        for(int i = 0;i < str.length();i++){
            if(delimiters.keySet().contains(str.charAt(i))) stack.push(str.charAt(i));
            else if(delimiters.values().contains(str.charAt(i))){
                if(!stack.empty() && delimiters.get(stack.peek()) == str.charAt(i)) stack.pop();
            else return "NO";
        }
      }
      
        return stack.empty() ? "YES" : "NO";
    }

}