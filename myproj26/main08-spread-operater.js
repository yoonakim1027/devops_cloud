// const [name, ...rest] = ['tom', 10, 'seoul']
// // 이렇게 하면? 

// console.log(name);
// console.log(rest);



const numbers = [1.2, 3];

const new_numbers = [
    10, 20, 30,
    ...numbers,
    40, 50, 60,
    ...numbers,
    70, 80, 90,
    ...numbers,
];

console.log(new_numbers);


// 새로운 steve를 만드려면?

const tom = {
    "name": "Tom",
    "age": 10,
    "region": "seoul",
};

const steve = {
    ...tom, // js에서는 전개(spread)
    name: "Steve"
};

// tom에 있는 값들을 참조해서, 그대로 steve가 만들어짐
// 여기서 이름을 steve로 바꿔주고싶다면? 

console.log(steve);