// const foo = () => {
//     let a = b = 10
//     a++;
//     return a;
// }

// foo()

// console.log(a);
// console.log(b);

// const arr1 = ['a', 'b', 'c']
// const arr2 = ['b', 'c', 'a']
// console.log(
//     arr1.sort() === arr1,
//     arr2.sort() == arr2,
//     arr1.sort() === arr2.sort(),
//     arr1.sort(),
//     arr2.sort()
// );

// function processReading(readings){
//     let low = Math.min()
//     let sum = 0
//     for (let i = 0; i < readings.length; i++) {
//         sum += readings[i]
//         if (low > readings[i]) {
//             low = readings[i]
//         }        
//     }
//     const avg = sum/readings.length

//     let high = Math.max()
//     for (let j = 0; j < readings.length; j++) {
//         if (high < readings[j]) {
//             high = readings[j]
//         }        
//     }

//     const first = readings[0]
//     const last = readings[readings.length-1]

//     return {first, last, low, high, avg}

// }

// readings = [121, 132, 127, 124, 174, 125]
// console.log(processReading(readings));


// function displayWordUnderscores(){
//  var elem = document.getElementById("correctGuess")
//  if(guesses.length !== 0){
//     for(var i = 0; i < guesses.length; i++){
//         elem.innerHTML = guesses[i] + ' '
//     }
//  }
//  else{
//      elem.innerHTML = '_'
//  }
// }

console.log(3+3+'7');

arr = [
    1,
    2,
    3,
    [[[[[4]]]]],
    [5,[6,[7,[8]]]]
]

// function flatIt(){
//     return this.toString();
// }

// Array.prototype.flatten = flatIt;
// console.log(arr.flatten());
console.log(arr.toString());

x = Math.random(0, 1)
console.log(x);

arr = [
    {
        name: 'Satyam',
        age: 29,
    },
    {
        name: 'Sahil',
        age: 25
    },
    {
        name: 'Tarun',
        age: 29
    }
]

const data = arr.filter(ele => ele.name === 'Satyam')
console.log(data);