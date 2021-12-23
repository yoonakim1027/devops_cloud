const { melon_data: song_array } = require("./melon_data");


// TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은?
// Array의 filter와 reduce를 활용해주세요.


const top_like_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => {
        if (!acc || acc.like > song.like)
            return song;
        return acc;
    }, null);


console.log(top_like_song);



const top_song3 = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .reduce((acc, song) => { //매번 song이 넘어온다~ 
        return acc.like > song.like ? song : acc; //현재의 song을 acc에 남김
    });

console.log(top_song3);



// 방법 3 : min 함수 활용 
Array.prototype.min = function (key_fn) {
    return this.reduce((acc, song) => {
        return key_fn(acc) > key_fn(song) ? song : acc;
    }); // 최솟값의 속성이 바뀔 수 있음 
    // acc를 주면? acc.like
    // song을 주면? song.like 속성을 빼오면 됨 
}

const top_song4 = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .min(song => song.rank);
console.log(top_song4.title, top_song4.like);




