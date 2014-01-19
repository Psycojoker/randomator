function indexOf(arr, item, fromIndex) {
    fromIndex = fromIndex || 0;
    if (arr == null) {
        return -1;
    }

    var len = arr.length,
        i = fromIndex < 0 ? len + fromIndex : fromIndex;
    while (i < len) {
        // we iterate over sparse items since there is no way to make it
        // work properly on IE 7-8. see #64
        if (arr[i] === item) {
            return i;
        }

        i++;
    }

    return -1;
}

function remove(arr, item){
    var idx = indexOf(arr, item);
    if (idx !== -1) arr.splice(idx, 1);
}
