int missingNumber(int* nums, int numsSize){
    //the missing contain all 1+2+3+...+n
    int missing = numsSize*(numsSize+1)/2;
    
    //substract all then what will be left will be the missing
    for(int i = 0; i < numsSize; i++){
        missing -= nums[i];
    }
    return missing;
}