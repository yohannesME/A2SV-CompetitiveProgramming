
vector<int> countingSort(vector<int> arr) {
    vector<int> count;
    for(int i  = 0; i < 100; i++){
        count.push_back(0);
        for(int j = 0; j < arr.size(); j++){
            if(i == arr[j]){
                count[i]++;
            }
        }
    }
    return count;
}
