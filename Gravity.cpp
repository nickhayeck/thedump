#include <iostream>
#include <vector> 


struct _2d_vector{
  long double x;
  long double y;
};

struct point_mass{
  long double x;
  long double y;
  long double m;
};

std::vector<_2d_vector> newtons_change(long double time, std::vector<point_mass> a){
  std::vector<_2d_vector> out;
  _2d_vector current;
  const long double G = 6.6742E-11;
  for(int i = 0; i < a.size(); i++){
    current.x = 0;
    current.y = 0;
    for(int j = 0; j < a.size(); j++){
      if(i == j) continue;
      
      if(a[j].x == a[i].x) current.x += 0;
      else current.x += G*a[j].m*time*time / (2.0*(a[j].x - a[i].x)*(a[j].x - a[i].x));
      
      if(a[j].y == a[i].y) current.y += 0;
      else current.y += G*a[j].m*time*time / (2.0*(a[j].y - a[i].y)*(a[j].y - a[i].y));
    }
    out.push_back(current);
  }
  
  return out;  
}


int main(){
  point_mass a;
  point_mass b;
  point_mass c;
  a.x = 0;
  a.y = 0;
  a.m = 1E5;
  
  b.x = 1;
  b.y = -1;
  b.m = 1E10;
  
  c.x = 1E-3;
  c.y = 1E-3;
  c.m = 1E5;
  std::vector<point_mass> n = {a,c};
  
  std::vector<_2d_vector> q = newtons_change(5,n);
  for(auto elem : q){
    std::cout<<"("<<elem.x<<", "<<elem.y<<")"<<std::endl;
  }
}