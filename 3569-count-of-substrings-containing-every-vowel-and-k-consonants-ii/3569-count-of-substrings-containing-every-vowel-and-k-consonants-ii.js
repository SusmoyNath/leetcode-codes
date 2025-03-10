function countOfSubstrings(word, k) {
  return helper(word, k) - helper(word, k - 1);

  function helper(word, k) {
    const vowels = { a: 0, e: 0, i: 0, o: 0, u: 0 };
    let count = 0;
    let left = 0;
    let consonants = k;

    for (let right = 0; right < word.length; right++) {
      const character = word[right];
      if (character in vowels) {
        vowels[character]++;
      } else {
        consonants--;
      }

      while (vowels.a > 0 && vowels.e > 0 && vowels.i > 0 && vowels.o > 0
             && vowels.u > 0 && consonants < 0) {
        const leftCharacter = word[left];
        if (leftCharacter in vowels) {
          vowels[leftCharacter]--;
        } else {
          consonants++;
        }
        left++;
      }
      count += right - left + 1;
    }
    return count;
  }
}