const spinWords = sentence => {
  const b = [];
  const a = sentence.split(" ");
  for (let i = 0; i < a.length; i++){
    if (a[i].length >= 5){
      b.push(a[i].split('').reverse().join(""));
    } else {
      b.push(a[i]);
    }
  }
  return b.join(" ");
}
