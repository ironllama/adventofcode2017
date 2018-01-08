// Advent of Code 2017
// Day 1 - Part I
// Dart


import 'dart:async';
import 'dart:io';

void main() {
  new File("advent01.in").readAsString().then((String allFileStr) {
      int sumTotal = 0;
      for (int i = 0; i < allFileStr.length; i++) {
          String thisChar = allFileStr[i];
          String nextChar = allFileStr[(i + 1) % allFileStr.length];
          if (thisChar == nextChar) sumTotal += int.parse(thisChar);
      }

      print("Total: ${sumTotal}");
  });
}
