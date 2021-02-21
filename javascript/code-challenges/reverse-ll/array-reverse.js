'use strict';

const reverse = (list) => {
    let start = 0;
    let end = list.length - 1;
    while (start <= end) {
        let temp = list[start];
        list[start] = list [end];
        list[end] = temp;
        start ++;
        end --;
    }
};

module.exports = reverse;