class Solution {
private:
bool valid_ipv4(string str)
{
    int count = 0;//to count no of dots
    int temp_size=0;
    char prev='\0';
    int i =0;
    while(i< str.size())
    {
        char ch = str[i];
        string temp="";
        temp_size=0;
        while(i<str.size()&&str[i]!='.')
        {
            temp_size++;
            ch = str[i];
            if(!(ch>='0'&&ch<='9'))
            return false;
            temp+=ch;
            i++;
        }
        if(str[i]=='.'&&i==str.size()-1)
        return false;
        i++;
        if((temp_size==0)||temp_size>3||temp[0]=='0'&&temp_size>1)
        {
            return false;
        }
        count++;
        int value = stoi(temp);
        if(value<0||value>255)//check the value of part 
        return false;
    }
   
    if(count-1==3)
    return true;

    return false;

}
bool valid_ipv6(string str)
{
    int count = 0;
    int temp_size=0;
    int i =0;
    while(i< str.size())
    {
        char ch = str[i];
        string temp="";
        temp_size=0;
        while(i<str.size()&&str[i]!=':')
        {
            temp_size++;
            ch = str[i];
            if(!(ch>='0'&&ch<='9'||ch>='a'&&ch<='f'||ch>='A'&&ch<='F'))
            return false;
            temp+=ch;
            i++;
        }
        if(str[i]==':'&&i==str.size()-1)
        return false;
        i++;
        if(temp_size<1||temp_size>4)
        {
            return false;
        }
        count++;
    }

    if(count-1==7)
    return true;

    return false;
}
public:
    string validIPAddress(string str) {
        bool ipv4=false;
        bool ipv6=false;
        int ret=str.find('.');
        if(ret>=0&&ret<=str.size())
        {
            ipv4=valid_ipv4(str);
        }
        else{
            ipv6=valid_ipv6(str);
        }   
        if(ipv4)
        {
            cout<<"ipv4";
            return "IPv4";
        }
        else if(ipv6)
        {
            cout<<"ipv6";
            return "IPv6";
        }
        else 
        {
            cout<<"neither";
            return "Neither";
        }
    }
};