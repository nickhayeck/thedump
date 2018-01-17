#include <iostream>
#include <cmath>
#include <random>
#include <limits>

typedef unsigned long long bigInt;
bigInt modExp(bigInt b, bigInt e, bigInt m){
	bigInt remainder;
	bigInt x = 1;

	while (e != 0){
	remainder = e % 2;
	e= e/2;

	if (remainder == 1)
		x = (x * b) % m;
	b= (b * b) % m; // New base equal b^2 % m
	}
	return x;
	}

bool isPrime(bigInt number)
  {
     if(number == 0) return false;
     for (bigInt i=2; i<number; i++)
     { if(number % i==0)
       return false;
     }
     
     return true; //will return true otherwise
  }
bigInt primeGen(bool yes){
		std::random_device rd;   
    std::mt19937_64 eng(rd()); 
    std::uniform_int_distribution<unsigned long long> distr;
    std::uniform_int_distribution<long> distr1;
    if(yes){
    	bigInt num = 0;
    	while(!isPrime(num)){
    		num = distr(eng);
    	}
    	return num;
    }
    if(!yes){
    	bigInt num = 0;
    	while(!isPrime(num)){
    		num = distr1(eng);
    	}
    	return num;
    }
}

template<typename func, typename func1>
bigInt diffie_hellman(func pushToNet, func1 getFromNet, bool server){
	//pass two functions into, one for pushing to network, another for receiving the next bits;
	//return a shared key
	if(server){
		//generate g and p
		bigInt moduli = primeGen(true);
		bigInt base = primeGen(false);
		//generate a
		bigInt serverPower =  primeGen(true);
		//calculate g^a mod p
		bigInt serverKey = modExp(base,serverPower,moduli);
		pushToNet(base, moduli, serverKey);
		bigInt clientPublicKey = getFromNet();
		return modExp(clientPublicKey, serverPower, moduli);
		
		
	}else{
		bigInt base = getFromNet();
		bigInt moduli = getFromNet();
		//generate b
		bigInt clientPower =  primeGen(true);
		//calculate g^b mod p
		bigInt clientKey = modExp(base,clientPower, moduli);
		
		pushToNet(base, moduli, clientKey);
		


		
		bigInt serverPublicKey = getFromNet();
		return modExp(serverPublicKey,clientPower, moduli);
	}
}


void push(bigInt a, bigInt b, bigInt c ){
	std::cout<<"a:"<<a<<"\nb:"<<b<<"\nc:"<<c<<"\n\n";
}
bigInt pull(){
	bigInt a;
	std::cin>>a;
	return a;
}

int main(){
	std::cout<<diffie_hellman(push, pull, false);
	
	return 0;
}