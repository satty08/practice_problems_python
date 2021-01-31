// const foo = () => {
//     let a = b = 10
//     a++;
//     return a;
// }

// foo()

// console.log(a);
// console.log(b);

const arr1 = ['a', 'b', 'c']
const arr2 = ['b', 'c', 'a']
console.log(
    arr1.sort() === arr1,
    arr2.sort() == arr2,
    arr1.sort() === arr2.sort(),
    arr1.sort(),
    arr2.sort()
);