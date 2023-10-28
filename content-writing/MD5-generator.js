// content-writing/MD5-generator.js

function generateMD5(str) {
  const md5 = (str) => {
    let hash = crypto.createHash('md5').update(str).digest('hex');
    return hash;
  };

  if (typeof window === 'undefined') {
    const crypto = require('crypto');
    return md5(str);
  } else {
    return md5(str);
  }
}

