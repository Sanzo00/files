#include <iostream>
#include <fstream>
#include <vector>
#include <stdint.h>
#include <algorithm>
#include <unordered_set>
using namespace std;

typedef uint32_t VertexId; // vertex dta type
typedef float EdgeId;       // edge data type

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
    // std::cout << token << std::endl;
  }
  res.push_back(s.substr(start));  
  // std::cout << s.substr(start) << std::endl;
}

int getNum(int x, vector<VertexId> &nums) {
  return lower_bound(nums.begin(), nums.end(), x) - nums.begin();
  // return lower_bound(nums.begin(), nums.end(), x) - nums.begin() + 1;
}

struct pair_hash {
  inline std::size_t operator()(const std::pair<VertexId, VertexId> & v) const {
      return v.first * 31 + v.second;
  }
};


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
    
    // EdgeUnit<EdgeId> edge;
    // vector<EdgeUnit<EdgeId>> edges; 
    vector<VertexId> nums;
    std::unordered_set<std::pair<VertexId, VertexId>, pair_hash> hashmap_edges;
    uint64_t count = 0;
    if (!in.is_open()) {
      cout << fin << " open error!" << endl;
      exit(-1);
    }

    int line_cnt = 0;
    while (getline(in, line)) {

      if (line[0] == '#' || line[0] == '%') continue;
      // if (line[0] == '#' || line[0] != 'a') continue;
      if (++line_cnt % 10000000 == 0) {
        cout << "read " << line_cnt / 1000000 << "M edages." << endl;
      }

      split(line, " ", container);
      // split(line, "\t", container);


      // for (auto x : container) {
      //   std::cout << x << ' ';
      // } std::cout << std::endl;

      edge.src = (VertexId) std::stoi(container[0]);
      edge.dst = (VertexId) std::stoi(container[1]);

      // edge.src = (VertexId) std::stoi(container[1]);
      // edge.dst = (VertexId) std::stoi(container[2]);
      // printf("line %d %d %d\n", line_cnt, edge.src, edge.dst);
      // edge.edge_data = (EdgeId) std::stof(container[2]);
      // for (auto it : container) {
      //   std::cout << it << " ";
      // } std::cout << endl;
      // std::cout << edge.src << " " << edge.dst << " " << edge.edge_data << std::endl;

      nums.push_back(edge.src);
      nums.push_back(edge.dst);
      // cout << edge.src << " -> " << edge.dst << endl;
      // cout << edge.src << " " << edge.dst << " " << edge.edge_data << endl;
      VertexId u = edge.src;
      VertexId v = edge.dst;
      // edges.push_back({u, v});
      // edges.push_back({v, u});

      if (hashmap_edges.find({u, v}) == hashmap_edges.end()) {
        edges.push_back({u, v});
        hashmap_edges.insert({u, v});
      }

      // self loop
      if (hashmap_edges.find({u, u}) == hashmap_edges.end()) {
        edges.push_back({u, u});
        hashmap_edges.insert({u, u});
      }

      if (hashmap_edges.find({v, v}) == hashmap_edges.end()) {
        edges.push_back({v, v});
        hashmap_edges.insert({v, v});
      }

      // undirected edges
      if (hashmap_edges.find({v, u}) == hashmap_edges.end()) {
        edges.push_back({v, u});
        hashmap_edges.insert({v, u});
      }
    }
    std::cout << "from " << argv[1] << " read " << line_cnt << " lines" << std::endl;

    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    // self-loop
    // for (VertexId i = 0; i < nums.size(); ++i) {
    //   edges.push_back({i, i});
    // }

    cout << "vertex: " << nums.size() << " edges: " << edges.size() << endl;
    for (auto &e : edges) {
      e.src = getNum(e.src, nums);
      e.dst = getNum(e.dst, nums);
      // std::cout << e.src << " " << e.dst << " " << e.edge_data << std::endl;
      out.write((char*)&e, sizeof(e));
      if (++count % 10000000 == 0) {
        cout << "process " << count / 1000000 << "M edages." << endl;
      }
    }

    cout << "convert is done!" << endl;
    in.close();
    out.close();

  return 0;
}
