const { melon_data: song_array, melon_data } = require("./melon_data");

// console.log(song_array);



// for (const song of song_array) {
//     console.log(song.title); // title만 출력하기 
// }



// 간단하게 해볼 수 있는 것은? 
// 노래에 대한 제목, like

// TODO : Like 오름차순으로 정렬 


// for (const song of song_array) {
//     console.log(song.like, song.title); // title만 출력하기 
// }


/*
비교함수를 받음 -> 함수 
정렬순서를 정의하는 함수를 지정해야 함 
함수를 받으면 그 함수는 인자를 2개를 받음 
2개를 받아서 어떤 값을 리턴해주는 함수 
numbers.sort(함수를 지정) {
    인자를 받으면  ?= > 어떤 값을 리턴해주는 함수 (arrow)
}
((파이썬))
sorted(numbers, key=함수)

((자바스크립트))
numbers.sort(
    (a,b) => 어떤값이 크다 작다를 리턴해주는것
    a가 b보다 작으면 음수
    a가 b보다 크면 양수
    a-b로 구현했을때? b가 크면 음수 
    0보다 작은 경우가 a가 b보다 더 작은것
    같으면 0을 반환
    0보다 큰 경우는 a가 더 큰것이니까 a가 더 나중에 오도록 
    -> 오름차순으로 정렬 
    (인덱스0, 인덱스1)

)

기본적인 정렬방식은 0,1번째와 비교하고 
그다음 0과 2 / 0과 3 0과 4..
다시 이제 1과 2 1과 3 1과 4

sorting 알고리즘
사전처럼 정렬
큰수에서 작은수 / 작은수에서 큰수 ..
2개의 아이템을 선택 비교
왼쪽이 오른쪽보다 크면 교환
오른쪽으로 이동해서 계속 해당 프로세스를 반복
비교 / 스와핑 : 비교를 두개씩 비교 하고 계속 ...
파이썬은 정렬기준값을 만들어주면 알아서 하고
자바스크립트는 2개씩 끊어서비교하는것을 우리가 해야한다.

( 노마드 코더 영상 )

bubble sort dance 
두개씩 비교하는 것 

*/


/// 현재 melon_data가 저장된 변수는 song_array

const songs = song_array.sort(
    (song_array1, song_array2) => {
        return song_array1.like - song_array2.like;
    }

);
/* 그냥 songs 안에는 위의 값을 기준으로 정렬된 값만 들어가 있음.
 .sort()안의 (song_array1, song_array2)는 아까 bubble sorting 처럼 
 양옆의 값을 비교해서 song_array의 0번 인덱스 - 1번인덱스
 이렇게 비교를 해서 하나하나씩 들어가고, 
 return에서 song_array1과 song_array2를 서로 빼는 방식으로 뺀 다음에 
 왼쪽이 오른쪽보다 크면 교환
오른쪽으로 이동해서 계속 해당 프로세스를 반복
해서 저장된 값이 songs에 출력되는 것 
 */

for (const song1 of songs) {
    console.log(song1.like, song1.title);
}

// 현재 songs 는 array(배열)형태. 그래서 따로 songs.like이렇게 한다고 값이 출력되지 않음 

