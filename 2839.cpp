int answer = 100000000;

int solve(int n,int count){
    // std::cout<< n << " " << count <<std::endl;
    if(n == 0){
        answer = std::min(answer, count);
    }
    if(n >=3 ){
        solve(n-3,count+1);
    }
    if(n>=5){
        solve(n-5,count+1);
    }
    return 0;
}


int main(){
    int n;
    std::cin >> n;
    solve(n,0);
    std::cout << answer << std::endl;


}
