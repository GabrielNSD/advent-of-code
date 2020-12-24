const fs = require("fs");

const question1 = () => {
  fs.readFile("./input.txt", (err, data) => {
    console.time("aaa");
    if (err) {
      console.log("error");
    }
    const directions = data.toString();
    const directionsArray = directions.split("");
    const answer = directionsArray.reduce((acc, currentValue) => {
      if (currentValue === "(") {
        return (acc += 1);
      } else if (currentValue === ")") {
        return (acc -= 1);
      }
    }, 0);
    console.log(answer);
    console.timeEnd("aaa");
  });
};

const question2 = () => {
  fs.readFile("./input.txt", (err, data) => {
    console.time("bbb");
    if (err) {
      console.log("error");
    }
    const directions = data.toString();
    const directionsArray = directions.split("");
    let accumulator = 0;
    let counter = 0;
    const answer = directionsArray.some((currentValue) => {
      if (currentValue === "(") {
        accumulator += 1;
      } else if (currentValue === ")") {
        accumulator -= 1;
      }
      counter++;
      return accumulator < 0;
    });
    console.timeEnd("bbb");
    console.log(counter);
  });
};

question2();

question1();
