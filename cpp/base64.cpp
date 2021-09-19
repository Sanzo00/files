#include <iostream>
#include <bitset>
#include <vector>
#include <cstring>

const char* base64_chars = {
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  "abcdefghijklmnopqrstuvwxyz"
  "0123456789"
  "+/"
};

std::string base64_encode(const char* bytes_to_encode, const int len) {
  int len_encode = (len + 2) / 3 * 4;
  std::string ret;
  ret.reserve(len_encode);
  int pos = 0;
  char tail = '=';
  while (pos < len) {
    ret.push_back(base64_chars[(bytes_to_encode[pos] & 0xfc) >> 2]);
    if (pos + 1 < len) {
      ret.push_back(base64_chars[((bytes_to_encode[pos] & 0x03) << 4) + ((bytes_to_encode[pos + 1] & 0xf0) >> 4)]);
      if (pos + 2 < len) {
        ret.push_back(base64_chars[((bytes_to_encode[pos + 1] & 0x0f) << 2) + ((bytes_to_encode[pos + 2] & 0xc0) >> 6)]);
        ret.push_back(base64_chars[bytes_to_encode[pos + 2] & 0x3f]);
      } else {
        ret.push_back(base64_chars[(bytes_to_encode[pos + 1] & 0x0f) << 2]);
        ret.push_back(tail);
      }
    } else {
      ret.push_back(base64_chars[(bytes_to_encode[pos] & 0x03) << 4]);
      ret.push_back(tail);
      ret.push_back(tail);
    }
    pos += 3;
  }
  return ret;
}

int pos_of_char(char c) {
  if (c >= 'A' && c <= 'Z') {
    return c - 'A';
  } else if (c >= 'a' && c <= 'z') {
    return c - 'a' + 'Z' - 'A' + 1;
  } else if (c >= '0' && c <= '9') {
    return c - '0' + 'Z' - 'A' + 'z' - 'a' + 2;
  } else if (c == '+') {
    return 62;
  } else if (c == '/'){
    return 63;
  } else {
    std::cout << "wrong format!" << std::endl;
    exit(1);
  }
  return -1;
}

std::string base64_decode(const char* bytes_to_decode, const int len) {
  int len_decode = len / 4 * 3;
  int pos = 0;
  std::string ret;
  ret.reserve(len_decode);
  while (pos < len) {
    ret.push_back((pos_of_char(bytes_to_decode[pos]) << 2) + ((pos_of_char(bytes_to_decode[pos + 1]) & 0x30) >> 4));
    if (pos + 2 < len && bytes_to_decode[pos + 2] != '=') {
      ret.push_back(((pos_of_char(bytes_to_decode[pos + 1]) & 0x0f) << 4) + ((pos_of_char(bytes_to_decode[pos + 2]) & 0x3c) >> 2));
      if (pos + 3 < len && bytes_to_decode[pos + 3] != '=') {
        ret.push_back(((pos_of_char(bytes_to_decode[pos + 2]) & 0x03) << 6) + pos_of_char(bytes_to_decode[pos + 3]));
      } // =
    } // ==
    pos += 4;
  }
  return ret;
}

int main(int argc, char** argv) {

  // if (argc < 2) {
  //   std::cout << "./base64 string" << std::endl;
  //   exit(1);
  // }
  
  std::string src = "0LCJpZCI6ImJhMzE0Y2EwLWU2OTQtNDhlYS1hZWEwLWYzNDBkMWRjZGEzZSIsIm5ldCI6InRjcCIsInBvcnQiOjI1MjYyLCJwcyI6ImlwdjYtMjUyNjIiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoibm9uZSIsInYiOj@#";
  std::cout << "src:" << std::endl;
  std::cout << src << std::endl;

  std::cout << "base64_encode:" << std::endl;
  std::string src_encode = base64_encode(src.c_str(), src.size());
  std::cout << src_encode << std::endl;

  std::cout << "base64_decode:" << std::endl;
  std::string src_decode = base64_decode(src_encode.c_str(), src_encode.size());
  std::cout << src_decode << std::endl;

  return 0;
}
