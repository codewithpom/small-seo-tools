// column data is a string

function row_to_delimited(data, deli) {
  // split the column data into an array of strings
  // join the array of strings with a comma
  // return the joined string
  return data.split("\n").join(deli);
}

function delimited_to_row(data, deli) {
  // split the column data into an array of strings
  // join the array of strings with a comma
  // return the joined string
  return data.split(deli).join("\n");
  
}