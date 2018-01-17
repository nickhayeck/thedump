#include <iostream>
#include <cstdio> 
#include <vector>
#include <cstdarg> 

/*! Relatively Simple C++ Class for Tensor Operations */
template <class T>
class Tensor{
	private:
		std::vector<T> elems;
	public:
		std::vector<int> dimensions;

		//constructor
		Tensor(std::vector<int> size) { 
				int dimSum = 1;
				for(int i = 0; i < size.size(); i++){
					dimensions.push_back(size.at(i));
					dimSum*= size.at(i);
					
				}
				for(int i = 0; i < dimSum; ++i){
					elems.push_back(NULL);
				}
    } 
		//functions: add (adds two tensors), mult(multiplies), get, set, noiseFill (fills with noise)
		Tensor<T> add(Tensor a);
		Tensor<T> mult(Tensor a);
		T get(std::vector<int> location);
		void set(std::vector<int> location, T value);
		void noise_fill();

	
};

//get
template<class T>
T Tensor<T>::get(std::vector<int> location){
	if(location.size() == dimensions.size()){
	int accesser = 0;
	for(int i = 0; i < location.size(); ++i){
		int currentArg = location.at(i)-1;
		signed int currentMax = i-1;
		while(currentMax > -1){
			currentArg *= dimensions.at(currentMax);
			currentMax--;
		}
		accesser+= currentArg;
	}
	return elems.at(accesser);
	}else{
		perror("Location vector size is not equal to the dimensions vector size");
    exit (EXIT_FAILURE);

	}
}

//set
template<class T>
void Tensor<T>::set(std::vector<int> location, T value){
	if(location.size() == dimensions.size()){
	int accesser = 0;
	for(int i = 0; i < location.size(); ++i){
		int currentArg = location.at(i)-1;
		signed int currentMax = i-1;
		while(currentMax > -1){
			currentArg *= dimensions.at(currentMax);
			currentMax--;
		}
		accesser+= currentArg;
	}
	elems.at(accesser) = value;
	}else{
		throw std::invalid_argument("Input vector and Tensor are not of same size");
    exit (EXIT_FAILURE);

	}
}


//add
template<class T>
Tensor<T> Tensor<T>::add(Tensor a){
	if(this.dimensions == a.dimensions){ 
  	Tensor<T> output = new Tensor<T>(this.dimensions);
  	for(T y : this.elems){
  		for(auto x : a.elems){
  			output.elems.push_back(x + y);
  		}	
  	}	
	}else{
		throw std::invalid_argument("Tensors are not of same size");
	}
	
}

//noiseFill

template<class T>
void Tensor<T>::noise_fill(){
	
	
}



int main(){
	Tensor<int> n({10000000});
	n.set({40000},10);
	std::cout<<n.get({40000})<<std::endl;
	return 0;
}