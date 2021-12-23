const { melon_data: song_array } = require("./melon_data");


// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.


const top_like_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => {
        if (!acc || acc.like < song.like)
            return song;
        return acc;
    }, null);


console.log(top_like_song);



const top_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => { //매번 song이 넘어온다~ 
        if (!acc) return song; //현재의 song을 acc에 남김
        else if (acc.like < song.like)// acc에는 song에 대한 정보가 남아있음 
            return song;
        else
            return acc;
        // 기존의 song.like와 새로들어온 song.like가 더 크다면? return
    }, null);

// acc: null 곡1의 like = 100 
// 그러면 acc에는 곡1이라는 객체로만 남음
// acc : 곡1(100) 곡2(200) => acc에는 곡 2가 남음


const top_song2 = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => { //매번 song이 넘어온다~ 
        if (acc.like < song.like)
            return song; //현재의 song을 acc에 남김
        else // 조건이 거짓일때 acc
            return acc;
        // 기존의 song.like와 새로들어온 song.like가 더 크다면? return
    });



const top_song3 = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => { //매번 song이 넘어온다~ 
        return acc.like < song.like ? song : acc; //현재의 song을 acc에 남김
    });

console.log(top_song3);



// 방법 3 : max 함수 활용 
Array.prototype.max = function (key_fn) {
    return this.reduce((acc, song) => {
        return key_fn(acc) < key_fn(song) ? song : acc;
    }); // 최솟값의 속성이 바뀔 수 있음 
    // acc를 주면? acc.like
    // song을 주면? song.like 속성을 빼오면 됨 
}

const top_song4 = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .max(song => song.like);
console.log(top_song4.title, top_song4.like);



