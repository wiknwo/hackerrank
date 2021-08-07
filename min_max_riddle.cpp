vector<long> riddle(vector<long> arr) {
    arr.push_back(-1);
    int n = arr.size(), i = 0;
    vector<long> res(n-1);
    stack<long> st;
    while(i < n){
        if(st.empty() || arr[i] > arr[st.top()]) st.push(i++);
        else{
            long val = arr[st.top()]; st.pop();
            int len = st.empty() ? i : i-st.top()-1;
            res[len-1] = max(val, res[len-1]);
        }
    }
    for(int i = n-3; i >= 0; --i)
        res[i] = max(res[i], res[i+1]);
    return res;
}