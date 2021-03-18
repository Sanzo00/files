#include <iostream>
#include <fstream>
#include <vector>
#include <stdint.h>
#include <algorithm>
using namespace std;

typedef uint32_t VertexId;
typedef uint64_t EdgeId;

struct Empty {};

template <typename EdgeData>
struct EdgeUnit {
  VertexId src;
  VertexId dst;
  EdgeData edge_data;
} __attribute__((packed));

template <>
struct EdgeUnit <Empty> {
  VertexId src;
  union {
    VertexId dst;
    Empty edge_data;
  };
} __attribute__((packed));

void split(string s, string delimiter, vector<string> &res) {
  size_t start = 0, end, delim_len = delimiter.length();
  string token;
  res.clear();

  while ((end = s.find(delimiter, start)) != string::npos) {
    token = s.substr(start, end - start);
    start = end + delim_len;
    res.push_back(token);
  }
  res.push_back(s.substr(start));  
}

int getNum(int x, vector<VertexId> &nums) {
  return lower_bound(nums.begin(), nums.end(), x) - nums.begin();
  // return lower_bound(nums.begin(), nums.end(), x) - nums.begin() + 1;
}

int main(int argc, char **argv) {
  if (argc < 3) {
    cout << "Usage: ./convert input output\n"; 
    exit(-1);
  }

    char *fin = argv[1];
    char *fout = argv[2];
    cout << "input: " << fin << endl;
    cout << "output: " << fout << endl;

    std::ifstream in(fin);
    std::ofstream out(fout, ios::binary);

    string line;
    vector<string> container;
    EdgeUnit<Empty> edge;
    vector<EdgeUnit<Empty>> edges;
    // EdgeUnit<VertexId> edge;
    // vector<EdgeUnit<VertexId>> edges; 
    vector<VertexId> nums;
    uint64_t count = 0;
    if (!in.is_open()) {
      cout << fin << " open error!" << endl;
      exit(-1);
    }

    while (getline(in, line)) {
      if (line[0] == '#') continue;
      split(line, "\t", container);
      // if (line[0] == '#' || line[0] != 'a') continue;
      // split(line, " ", container);
      edge.src = (VertexId) std::stoi(container[0]);
      edge.dst = (VertexId) std::stoi(container[1]);
      // edge.edge_data = (VertexId) std::stoi(container[3]);

      nums.push_back(edge.src);
      nums.push_back(edge.dst);
      // cout << edge.src << " -> " << edge.dst << endl;
      // cout << edge.src << " " << edge.dst << " " << edge.edge_data << endl;
      edges.push_back(edge);
    }

    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    cout << "vertex: " << nums.size() << " edges: " << edges.size() << endl;
    for (auto &e : edges) {
      e.src = getNum(e.src, nums);
      e.dst = getNum(e.dst, nums);
      out.write((char*)&e, sizeof(e));
      if (++count % 1000000 == 0) {
        cout << "process " << count / 1000000 << "M edages." << endl;
      }
    }

    cout << "convert is done!" << endl;
    in.close();
    out.close();

  return 0;
}