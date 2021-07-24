function getLetter(s) {
    var letter = ''
    var a_set = new Set(['a','e','i','o','u']);
    var b_set = new Set(['b','c','d','f','g']);
    var c_set = new Set(['h','j','k','l','m']);
    var d_set = new Set(['n','p','q','r','s','t','v','w','x','y','z']);

    // Write your code here
    switch(true) {
        case a_set.has(s[0]):
            letter = 'A'
            break
        case b_set.has(s[0]):
            letter = 'B'
            break
        case c_set.has(s[0]):
            letter = 'C'
            break
        case d_set.has(s[0]):
            letter = 'D'
            break
    }
    return letter;
}