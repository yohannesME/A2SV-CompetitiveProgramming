vector<int> gradingStudents(vector<int> grades) {
    vector<int> n;
    for(int i = 0; i < grades.size(); i++){
        if(grades[i] >= 38){
            if(grades[i]%5 >= 3){
                n.push_back(((int)(grades[i]/5)+1)*5);
            }else {
            n.push_back(grades[i]);
        }
        }
        else {
            n.push_back(grades[i]);
        }
    }
    return n;
}
