import { createInterface } from "readline";
import { readFile } from "node:fs";
import { writeFile } from "node:fs";

let readline = createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline.question("File Name: ", function (filename) {
  readline.close();
  readFile(
    `${filename}`,
    "ASCII",
    (err, message) => {
      if (err) {
        return console.log(err);
      }
      console.log(message.toUpperCase());
    }
  );
});




//med1

