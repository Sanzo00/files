#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector> 
const int N = 1000000;

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
  int count = 0;
  std::unordered_set<int> nodes;
  std::vector<std::pair<int,int>> edges;
  while (inFile.read(reinterpret_cast<char*>(&u), sizeof(int))) {
    inFile.read(reinterpret_cast<char*>(&v), sizeof(int));
    edges.push_back({u, v});
    nodes.insert(u);
    nodes.insert(v);

    if (++count % (N * 10) == 0) {
      printf("flush %dM edges\n", count / N);
      for (auto& p : edges) {
        outFile << p.first << " " << p.second << "\n";
      }
      edges.clear();
    }
  }

  if (!edges.empty()) {
    for (auto& p : edges) {
      outFile << p.first << " " << p.second << "\n";
    }
    edges.clear();
  }
  std::cout << "nodes: " << nodes.size() << " edges: " << count << std::endl;

  inFile.close();
  outFile.close();

  return 0;
}
