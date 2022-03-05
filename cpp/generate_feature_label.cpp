#include <iostream>
#include <fstream>
#include <string>
#include <vector>
const int N = 1000000;
int main(int argc, char** argv) {
  
  srand(time(0));

  if (argc < 5) {
    std::cout << "Usage ./a.out output node_num length range" << std::endl;
    exit(1);
  }
  
  int nodes = std::stoi(argv[2]);
  int length = std::stoi(argv[3]);
  int range = std::stoi(argv[4]);

  std::cout << "output: " << argv[1] << std::endl;
  std::cout << "node_num: " << nodes << std::endl;
  std::cout << "length: " << length << std::endl;
  std::cout << "range: " << range << std::endl;
  std::ofstream out(argv[1]);

  std::vector<std::vector<int> > buffer;
  for (int i = 0; i < nodes; ++i) {
    std::vector<int> vec(length + 1);
    vec[0] = i;
    for (int i = 1; i <= length; ++i) {
      vec[i] = rand() % range;
    }
    buffer.push_back(vec);

    // flush buffer
    if (i > 0 && i % (N * 10) == 0) {
      printf("flush %dM vector\n", i / N);
      for (auto& V : buffer) {
        for (int i = 0; i <= length; ++i) {
          if (i > 0) {
            out << " ";
          }
          out << V[i];
        }
        out << std::endl;
      }
      buffer.clear();
    }
  }

  if (!buffer.empty()) {
    for (auto& V : buffer) {
      for (int i = 0; i <= length; ++i) {
        if (i > 0) {
          out << " ";
        }
        out << V[i];
      }
      out << std::endl;
    }
    buffer.clear();
  }
  std::cout << "generate is done!" << std::endl;

  out.close();

  return 0;
}