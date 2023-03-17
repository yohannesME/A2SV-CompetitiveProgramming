class Solution {
    	string oneth[10] = {"Zero", "One",  "Two",  "Three",  "Four",  "Five",  "Six",  "Seven",  "Eight",  "Nine"};
	string tenth1[10] = {"Ten", "Eleven",  "Twelve",  "Thirteen",  "Fourteen",  "Fifteen",  "Sixteen",  "Seventeen",  "Eighteen",  "Nineteen"};
	string tenth[10] = {" "," ", "Twenty",  "Thirty",  "Forty",  "Fifty",  "Sixty",  "Seventy",  "Eighty",  "Ninety"};
	string finals[10] = {"Hundred","Thousand", "Million", "Billion", "Trillion" };
	
	
string response = "";

void hundreds(int n){
	
	int l;
	
	if(n/10 == 0){
		   // cout << oneth[n];	
        response += oneth[n] + " ";
	}
	else if(n/100 == 0){

		l = n%10;
		n = n/10;

		if (n == 1){
			// cout << tenth1[l] ;
            response+= tenth1[l] + " ";
		}
		else{
		// cout << tenth[n] << " " ;
        response+= tenth[n]+" ";
        
		if(l!=0)
		// cout << oneth[l] ;
            response+= oneth[l] + " ";
		}
	}
}

void thousand(int n){

	int l;
	
	if(n/100 == 0)
		   hundreds(n);
	else if(n/1000 == 0){

		l = n%100;
		n = n/100;
		
		// cout << oneth[n] << " " << finals[0] << " ";
        response+= oneth[n] + " " + finals[0] + " ";
		if(l != 0)
			hundreds(l);
	}
}



void million(int n){
	
	int l;
	
	if(n/1000 == 0)
		   thousand(n);
	else if(n/1000000 == 0){
		l = n%1000;
		n = n / 1000;
		if(l != 0){
			thousand(n);
			// cout << " " << finals[1] << " ";
            response +=  finals[1] + " ";
			thousand(l);
		}else{

        thousand(n);
            response+=finals[1] + " ";
			// cout << oneth[n] << " " << finals[0] << " " << finals[1]  << endl;
        }
	}
}


void billion(int n){
	int l;
	
	if(n/1000000 == 0){
		million(n);
	}
	else if(n/1000000000 == 0){
		l = n%1000000;
		n = n / 1000000;

		thousand(n);
		
		if(l != 0){
			// cout << " " << finals[2] << " " ;
            response += finals[2] + " ";
			million(l);
		}
		else
			// cout << " " << finals[2];	
        response+= finals[2];
	}
}

void trillion(int n){
	int l;
	
	if(n/1000000000 == 0){
		billion(n);	
	}
	else if(n/1000000000000 == 0){
		l = n%1000000000;
		n = n / 1000000000;

		million(n);
		
		if(l != 0){
			// cout << " " << finals[3] << " " ;
            response+= finals[3] + " ";
			billion(l);
		}
		else
			// cout << " " << finals[3];
            response+= finals[3];
	}
	
}


public:
    string numberToWords(int num) {
        trillion(num);

        if(response[response.length()-1]==' ')
            response.pop_back();
        return response;
    }
};