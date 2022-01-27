#include <fstream>
#include <iostream>

int main(int argc, char **argv) {

  if (argc < 3) {
    printf("Usage: ./convert input output\n");
    exit(-1);
  }
  
  std::ifstream inFile(argv[1], std::ios::in | std::ios::binary);
  if (!inFile.is_open()) {
    std::cout << argv[1] << " not exist!" << std::endl;
    exit(-1);
  }

  std::ofstream outFile(argv[2], std::ios::out);
  if (!outFile.is_open()) {
    std::cout << argv[2] << " create failed!" << std::endl;
    exit(-1);
  }

  int u, v;
  int edges = 0;
  while (inFile.read(reinterpret_cast<char*>(&u), sizeof(int))) {
    inFile.read(reinterpret_cast<char*>(&v), sizeof(int));
    edges++;
    outFile << u << " " << v << "\n";
  }
  std::cout << "edges: " << edges << std::endl;

  inFile.close();
  outFile.close();

  return 0;
}