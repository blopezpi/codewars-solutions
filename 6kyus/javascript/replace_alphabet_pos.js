const alph = {};
const arr = 'abcdefghijklmnopqrstuvwxyz'.split('');
for (let i = 0; i < arr.length; i++) {
 alph[arr[i]] = i + 1;
}

const alphabetPosition = text => {
  let num = [];
  let arr = text.toLowerCase().split('');
  for (let i = 0; i < arr.length; i++){
    if (alph[arr[i]]) {
      num.push(alph[arr[i]]);
    }  
  }
  return num.join(' ');
}
