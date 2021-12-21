const { question } = require("readline-sync");

const animal_names = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"];

animal_names
    .map((name) => {
        return {
            name: name, //name이라는 값을 리턴
            value: Math.random(),
        }//사전을 리턴
    })



// const random_animal_name = animal_names
//     .map((name)=>({
//         name,
//         value : Math.random(),
//     }))
//     .sort((a,b) => { //sort는 항상 인자가 2개(object를 받음 )
//         return obj_a.value - obj_b.value;

//     })

//     .map(obj => {
//         return obj.value;
//     });


// 원래 sorting 할 때에는 값을 2개씩 비교 
// 항상 두개씩 비교


// -> 위의 로직을 줄여본다면? 
const shuffled_animal_name = animal_names
    .map((name) => ({
        name,
        value: Math.random(),
    }))
    .sort((obj_a, obj_b) => { //sort는 항상 인자가 2개(object를 받음 )
        return obj_a.value - obj_b.value;
    })

    .map(({ name }) => name);

// for (const animal_names of shuffled_animal_name.slice(0, 5)) {
//     console.log(animal_names);
// }
//이렇게 map부분을 축약할 수 있음 

// javascript의 slice도 마지막값을 포함하지 않음


// timestamp : 1970년 1월 1일부터 몇초가 지났는지

// new Date() // 정확한 현재 시각 -> 날짜관련된 처리를 도와주는 자바스크립트의 기능
const begin_time = new Date().getTime(); // 현재 초단위
let ok_counter = 0; // 값을 증가시킬거니까 let

for (const animal_names of shuffled_animal_name.slice(0, 5)) {
    const line = question(`>>>>>: ${animal_names}>>>>`);

    if (line === animal_names) {
        ok_counter++;
    }
}

const end_time = new Date().getTime();
const time = end_time - begin_time;

console.log(`총 ${parseInt(time / 1000)}초가 걸렸습니다.`);
console.log(`총 ${ok_counter}회 맞췄습니다.`);