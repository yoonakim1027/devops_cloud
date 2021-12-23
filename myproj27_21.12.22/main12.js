const { melon_data: song_array } = require("./melon_data");


// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set
/*
계산하기 위해서 어떤 데이터를 만들어내야할까 ?
하나의 오브젝트에 ? 
{
    "가수1" : 2,
    "가수2" : 10,... 
    이런 형태의 오브젝트르 만들고 싶다면?
    어느 가수가 몇 곡이 있는지 합산이 될 것 
    합산이 되고 나면? 키인 "가수"는 필요하지 않음

}

- 파이썬에서는 없는 키에 접근하면 키에러가 발생함

*/
// 2시 05분경 
const artist_count_object = song_array //앞의 값은 acc, 우리는 계속 song을 가져올 것 
    .reduce((acc, { artist }) => {
        //       if (!acc[artist]) acc[artist] = 0;
        // 거짓이면 0으로 채우고, 거짓이아니면 그대로 있는 것 
        acc[artist] = acc[artist] || 0; // = 참이면 acc[artist]값을 활용, 거짓이면 0을 대입 (||은 or임)
        acc[artist] += 1;
        return acc;
        // 값이 undefined는 False(거짓)

    }, {}); // 두개의 {}는 서로 독립적!
// 반환이 {} 오브젝트가 되는 것 
// reduce의 리턴 값이 오브젝트
// 값으로는 횟수 -> 몇번 나왔는지? 


console.log(artist_count_object);


const artist_count_object1 = song_array
    .reduce((acc, { artist }) => {
        acc[artist] ||= 0
        acc[artist] += 1;
        return acc;
    }, {});


const total = Object.values(artist_count_object1)
    .filter(count => count >= 2)
    .length;


console.log(total);


/*
파이썬의 사전의 values() = Object.values(obj) <- 값만 있음




*/


// 숫자로만 구성된 배열이 리턴 -> array면 .length가 가능 
Object.values(artist_count_object)
    .filter(number => number >= 2)
    .length;



