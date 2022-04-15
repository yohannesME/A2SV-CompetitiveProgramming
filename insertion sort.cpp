void insertionSort1(int n, vector<int> arr) {
    int i, key, j;
    key = arr[arr.size()-1];
    for (i = arr.size()-2; i >=0; i--)
    {

        j = i ;
 
        if ( arr[j] > key)
        {   
                arr[j + 1] = arr[j];
                j = j - 1;

            for(int i = 0; i< arr.size(); i++){
                cout << arr[i] << " ";
                }
            cout << endl;            
        }
        else{
            arr[j + 1] = key;
            for(int i = 0; i< arr.size(); i++){
                cout << arr[i] << " ";
            }
            cout << endl;
            
            break;
        }
        if(i==0){
            arr[0] = key;
            
                        for(int i = 0; i< arr.size(); i++){
                cout << arr[i] << " ";
            }
            cout << endl;
        }
            
    }
}
