function getCount(str) {
  found = str.match(/[aeiou]/g);
  return found ? found.length : 0;
}
