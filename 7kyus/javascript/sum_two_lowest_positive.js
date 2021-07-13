function compareNumbers(a, b) {
  return a - b;
}

const sumTwoSmallestNumbers = numbers => {  
  let result = numbers.sort(compareNumbers);
  return result[0] + result[1];
}
